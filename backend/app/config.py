from __future__ import annotations

import os
from pathlib import Path


BACKEND_DIR = Path(__file__).resolve().parents[1]
PROJECT_ROOT = BACKEND_DIR.parent
DEFAULT_SQLITE_PATH = BACKEND_DIR / "bdo.db"


def database_url() -> str:
    """Return the configured SQLAlchemy URL, defaulting to a local SQLite file."""

    return os.getenv("DATABASE_URL", f"sqlite:///{DEFAULT_SQLITE_PATH.as_posix()}")


def seed_dir() -> Path:
    return PROJECT_ROOT / "data"

