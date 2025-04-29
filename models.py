from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.orm import Mapped, mapped_column
from database import Base


class WorkerOrm(Base):
    __tablename__ = "workers"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]


meta_obj = MetaData()

worker_table = Table(
    "workers",
    meta_obj,
    Column("id", Integer, primary_key=True),
    Column("username", String),
)
