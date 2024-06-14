import os

from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker

from infra.Data.Base import Base

load_dotenv()
from sqlalchemy import create_engine

connection_string = os.getenv("connection_string")
engine = create_engine(connection_string, echo=True)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)


def create_tables():
    Base.metadata.create_all(bind=engine)
