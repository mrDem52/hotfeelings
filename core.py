from sqlalchemy import text, select, insert
from database import sync_engine, async_engine
from models import meta_obj, worker_table


def get_1_sync():
    with sync_engine.connect() as conn:
        res = conn.execute(text('SELECT 1,2,3 union 4,5,6'))
        print(f"{res.first()=}")


async def get_1_async():
    async with async_engine.connect() as conn:
        res = await conn.execute(text('SELECT 1,2,3 union 4,5,6'))
        print(f"{res.first()=}")


class SyncCore:
    @staticmethod
    def create_tables():
        sync_engine.echo = False
        meta_obj.drop_all(sync_engine)
        meta_obj.create_all(sync_engine)
        sync_engine.echo = True

    @staticmethod
    def insert_workers():
        with sync_engine.connect() as conn:
            stmt = insert(worker_table).values(
                [
                    {"username": "Bob"},
                    {"username": "Mick"}
                ]
            )
            conn.execute(stmt)
            conn.commit()

    @staticmethod
    def select_workers():
        with sync_engine.connect() as conn:
            query = select(worker_table)
            result = conn.execute(query)
            workers = result.all()
            print(f"{workers}")
