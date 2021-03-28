from sqlalchemy import Column, String

from project_name.db import Base


class Example(Base):
    __tablename__ = "examples"
    test = Column(String)
