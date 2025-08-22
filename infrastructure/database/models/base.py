from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


# alembic revision --autogenerate -m "сообщени_миграции"