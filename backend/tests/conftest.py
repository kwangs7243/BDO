from __future__ import annotations

from collections.abc import Generator
from pathlib import Path

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from app.database import Base
from app.seed import import_seed


@pytest.fixture
def session() -> Generator[Session, None, None]:
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(engine)
    seed_path = Path(__file__).resolve().parents[2] / "data"
    with Session(engine, expire_on_commit=False) as db_session:
        import_seed(db_session, seed_path)
        yield db_session
    Base.metadata.drop_all(engine)

