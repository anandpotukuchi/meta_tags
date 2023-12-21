from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import create_engine, String, Text
engine = create_engine("mysql://root")

class Base(DeclarativeBase):
    pass

class Tags(Base):
    pass

