from sqlalchemy import text, insert
from database import sync_engine, async_engine, session_factory, async_session_factory
from models import meta_obj, WorkerOrm


def create_tables():
    sync_engine.echo = False
    meta_obj.drop_all(sync_engine)
    meta_obj.create_all(sync_engine)
    sync_engine.echo = True


def insert_data():
    with session_factory() as session:
        worker_man = WorkerOrm(username='Man')
        worker_woman = WorkerOrm(username='Woman')
        session.add_all([worker_man, worker_woman])
        session.commit()


async def insert_data():
    async with async_session_factory() as session:
        worker_man = WorkerOrm(username='Man')
        worker_woman = WorkerOrm(username='Woman')
        session.add_all([worker_man, worker_woman])
        await session.commit()
