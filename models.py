from sqlalchemy import Table, Column, Integer, String, MetaData

meta_obj = MetaData()


worker_table = Table(
    "workers",
    meta_obj,
    Column("id", Integer, primary_key=True),
    Column("username", String),
)