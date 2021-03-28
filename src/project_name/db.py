from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, MetaData, Sequence, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class EntityBase:
    # id = Column(UUID, primary_key=True, unique=True, server_default=text("uuid_generate_v1()"))
    id = Column(Integer, Sequence("id_seq"), primary_key=True)
    created_at = Column(
        "created_at", DateTime(timezone=True), default=datetime.now, nullable=False
    )
    modified_at = Column(
        "modified_at", DateTime(timezone=True), default=datetime.now, nullable=False
    )


Base = declarative_base(cls=EntityBase, metadata=MetaData())
