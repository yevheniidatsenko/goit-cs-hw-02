import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from typing import Generator
from sqlalchemy.orm import Session

# Retrieve the database URL from an environment variable, or use the default value
SQLALCHEMY_DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://zhenyadatsenko:124455@postgres:5432/hw_02"
)

# Creating the engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=True,
    max_overflow=5
)

# Creating the session class
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class for models
Base = declarative_base()

# Dependency function for obtaining the database session
def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()