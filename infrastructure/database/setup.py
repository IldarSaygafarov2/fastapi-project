from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from config.db import DbConfig


def create_engine(db: DbConfig, echo: bool = True):
    engine = create_async_engine(
        db.construct_url(),
        query_cache_size=1200,
        pool_size=20,
        max_overflow=200,
        future=True,
        echo=echo
    )
    return engine


def create_session_pool(engine):
    session_pool = async_sessionmaker(bind=engine, expire_on_commit=False)
    return session_pool


# инициализация миграций в проекте
# alembic init  -t async путь_до_папки_где_будут_храниться_миграции

