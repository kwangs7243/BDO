from app.main import get_user_content_state, put_user_content_state
from app.schemas import UserContentStateUpdate, UserContentStateValue


def test_user_content_state_persists_and_updates(session) -> None:
    initial = get_user_content_state("carrack-advance", session)
    assert initial.state == UserContentStateValue.NOT_STARTED
    assert initial.updated_at is None

    saved = put_user_content_state(
        "carrack-advance",
        UserContentStateUpdate(
            state=UserContentStateValue.FOUNDATION,
            priority=2,
            note="무역선 준비 상태 확인",
        ),
        session,
    )
    assert saved.state == UserContentStateValue.FOUNDATION
    assert saved.priority == 2
    assert saved.updated_at is not None

    updated = put_user_content_state(
        "carrack-advance",
        UserContentStateUpdate(
            state=UserContentStateValue.IN_PROGRESS,
            priority=1,
            note="다음 단계 조사 필요",
        ),
        session,
    )
    assert updated.state == UserContentStateValue.IN_PROGRESS
    assert get_user_content_state("carrack-advance", session).note == "다음 단계 조사 필요"

