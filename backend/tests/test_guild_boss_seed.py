import copy,json,shutil
from collections import Counter
from datetime import datetime,timezone
from pathlib import Path
from alembic import command
from alembic.config import Config
from sqlalchemy import create_engine,func,select
from sqlalchemy.orm import Session
from app.models import Content,Source,UserContentState
from app.seed import import_seed

DATA=Path(__file__).resolve().parents[2]/"data"
NEW_S={"guild-boss-guide-current","guild-boss-overhaul-2026-01-07","guild-boss-reset-rework-2019-12-04"}
NEW_C={"guild-boss-current-system","guild-boss-orgg","guild-boss-mogulis","guild-boss-ferrid","guild-boss-giant-mudster","guild-boss-gumiho-duoksini"}

def rows():
 return json.loads((DATA/"seed_sources.json").read_text(encoding="utf-8")),json.loads((DATA/"seed_contents.json").read_text(encoding="utf-8"))
def content(slug): return next(x for x in rows()[1] if x["slug"]==slug)
def reqs(slug): return {x["seed_key"].removeprefix(slug+"."):x for x in content(slug)["requirements"]}

def test_v19k_counts_references_and_sources():
 s,c=rows(); ids={x["id"] for x in s}; slugs={x["slug"] for x in c}
 assert (len(s),len(c),sum(len(x.get("relations",[])) for x in c))==(180,280,500)
 assert NEW_S<=ids and NEW_C<=slugs and "khan-guild-boss" in slugs
 assert all(x.get("status","active")=="active" for x in c)
 roles=Counter(x["structured_value"].get("knowledge_role") for y in c for x in y.get("requirements",[]) if isinstance(x.get("structured_value"),dict))
 assert {k:roles[k] for k in ("fact","strategy","measurement")}=={"fact":250,"strategy":63,"measurement":11}
 assert len({x["url"] for x in s})==len(s)
 assert {i for x in c for e in x.get("evidence",[]) for i in e["source_ids"]}<=ids
 assert {r["to_content_slug"] for x in c for r in x.get("relations",[])}<=slugs
 by={x["id"]:x for x in s}
 assert by["guild-boss-guide-current"]["url"].endswith("Wiki?wikiNo=171")
 assert by["marni-combat-analyzer-2026-08-05"]["title"]=="8월 5일(수) 업데이트 안내(최종 수정 : 2026-08-06 18:05)"

def test_v19k_system_semantics_and_no_misleading_checklist():
 r=reqs("guild-boss-current-system"); roster=r["roster"]["structured_value"]
 assert roster["standard_fragment_bosses"]==["khan-guild-boss","guild-boss-orgg","guild-boss-mogulis","guild-boss-ferrid","guild-boss-giant-mudster"]
 assert roster["ancient_puturum_current"] is False
 assert r["base-count"]["structured_value"]=={"knowledge_role":"fact","base_per_boss":1,"weekday":0,"time":"00:00","timezone":"Asia/Seoul","fragments_reset":True}
 recharge=r["recharge"]["structured_value"]
 assert (recharge["fame_cost"],recharge["per_boss_weekly"],recharge["satisfies_fragments"],recharge["separate_from_base"])==(25000,1,True,True)
 duo=r["duo-boundary"]["structured_value"]
 assert (duo["direct_summon"],duo["standard_recharge"],duo["weekly_limit"])==(True,False,1)
 h=content("guild-boss-current-system")
 assert h["checklists"]==[] and h["schedules"][0]["weekday"]==0 and h["schedules"][0]["time_local"]=="00:00"

def test_v19k_boss_mechanics_duo_identity_and_khan_stable_keys():
 assert reqs("guild-boss-orgg")["mechanics"]["structured_value"]["safe_zone"]=="yellow_circle"
 assert reqs("guild-boss-mogulis")["mechanics"]["structured_value"]["wild_golem_max"]==1
 assert reqs("guild-boss-ferrid")["mechanics"]["structured_value"]["ranged_knockdown_hits"]==2
 assert reqs("guild-boss-giant-mudster")["mechanics"]["structured_value"]["emergency_escape"] is True
 d=reqs("guild-boss-gumiho-duoksini")
 assert (d["access"]["structured_value"]["fame_cost"],d["access"]["structured_value"]["fame_reward"])==(25000,10000)
 assert d["identity"]["structured_value"]["separate_from_black_shrine"] is True
 assert {"donghae-shrine-gumiho","donghae-shrine-duoksini"}<={x["to_content_slug"] for x in content("guild-boss-gumiho-duoksini")["relations"]}
 k=content("khan-guild-boss"); keys={x["seed_key"] for x in k["requirements"]}
 assert {"khan-guild-boss.summon","khan-guild-boss.combat-tools","khan-guild-boss.death-penalty"}<=keys
 assert k["checklists"]==[] and all(x["structured_value"]["knowledge_role"]=="fact" for x in k["requirements"])

def baseline_contents(current):
 out=[copy.deepcopy(x) for x in current if x["slug"] not in NEW_C]; k=next(x for x in out if x["slug"]=="khan-guild-boss")
 k["summary"]="오킬루아의 눈에서 길드 소환 조각 5개로 진행하는 길드 우두머리다.";k["purpose"]="소환·전투 장비·회복 저지·핵심 전리품을 한 흐름으로 확인한다.";k["last_verified_at"]="2026-09-03"
 k["requirements"]=k["requirements"][:3]
 for x in k["requirements"]:x["structured_value"].pop("knowledge_role",None)
 k["requirements"][1]["description"]="길드 괴수 사냥 대포 조립 세트와 포탄을 사용한다. 흑결정 해초를 파괴하면 더 강한 흑결정 포탄을 마련할 수 있고 칸의 회복을 저지할 수 있다."
 k["requirements"][1]["structured_value"]={"equipment":["길드 괴수 사냥 대포 조립 세트","길드 괴수 사냥 대포알"],"black_crystal_seaweed":{"drop":"흑결정 포탄","purpose":"칸 체력 회복 저지"}}
 k["steps"]=[];k["rewards"]=k["rewards"][:3];k["rewards"][2].pop("amount_min",None);k["rewards"][2].pop("amount_max",None);k["sections"]=k["sections"][:1];k["relations"]=k["relations"][:1];k["evidence"]=k["evidence"][:5]
 for x in k["evidence"]:x["source_ids"]=["ocean-all-guide"]
 return out

def test_v19k_historical_import_idempotence_and_history(tmp_path,monkeypatch):
 db=tmp_path/"v19k.db";url=f"sqlite:///{db.as_posix()}";monkeypatch.setenv("DATABASE_URL",url)
 backend=Path(__file__).resolve().parents[1];cfg=Config(str(backend/"alembic.ini"));cfg.set_main_option("script_location",str(backend/"alembic"));command.upgrade(cfg,"20260902_0001");command.upgrade(cfg,"head")
 s,c=rows();bs=[copy.deepcopy(x) for x in s if x["id"] not in NEW_S];shared=next(x for x in bs if x["id"]=="marni-combat-analyzer-2026-08-05");shared["title"]="8월 5일(수) 업데이트 안내 - 마르니의 전투 분석기";shared.pop("notes",None)
 bd=tmp_path/"baseline";bd.mkdir();(bd/"seed_sources.json").write_text(json.dumps(bs,ensure_ascii=False),encoding="utf-8");(bd/"seed_contents.json").write_text(json.dumps(baseline_contents(c),ensure_ascii=False),encoding="utf-8");shutil.copy(DATA/"seed_projects.json",bd/"seed_projects.json")
 engine=create_engine(url)
 with Session(engine) as ss:
  import_seed(ss,bd);k=ss.scalar(select(Content).where(Content.slug=="khan-guild-boss"));stable=(k.id,{x.seed_key:x.id for x in k.requirements},{x.seed_key:x.id for x in k.rewards},{x.seed_key:x.id for x in k.sections})
  state=UserContentState(content_id=k.id,note="V1.9K history",updated_at=datetime(2026,9,8,tzinfo=timezone.utc));ss.add(state);ss.commit();sid=state.id
  import_seed(ss,DATA);counts=(ss.scalar(select(func.count()).select_from(Source)),ss.scalar(select(func.count()).select_from(Content)));import_seed(ss,DATA)
  now=ss.scalar(select(Content).where(Content.slug=="khan-guild-boss"))
  assert counts==(180,280)==(ss.scalar(select(func.count()).select_from(Source)),ss.scalar(select(func.count()).select_from(Content)))
  assert stable[0]==now.id
  assert stable[1]=={x.seed_key:x.id for x in now.requirements if x.seed_key in stable[1]}
  assert stable[2]=={x.seed_key:x.id for x in now.rewards if x.seed_key in stable[2]}
  assert stable[3]=={x.seed_key:x.id for x in now.sections if x.seed_key in stable[3]}
  assert ss.get(UserContentState,sid).note=="V1.9K history"



