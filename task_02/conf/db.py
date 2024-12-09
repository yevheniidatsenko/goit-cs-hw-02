import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Отримання URL бази даних з змінної середовища, або використання дефолтного значення
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://zhenyadatsenko:124455@postgres:5432/hw_02")

# Створення двигуна
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=True,  # Включити логування SQL-запитів (для розробки)
    max_overflow=5  # Максимальна кількість додаткових з'єднань
)

# Створення сесійного класу
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Базовий клас для моделей
Base = declarative_base()

# Функція залежності для отримання сесії бази даних
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()