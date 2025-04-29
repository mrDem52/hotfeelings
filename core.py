from sqlalchemy import text, insert
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






