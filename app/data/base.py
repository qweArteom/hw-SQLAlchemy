from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import create_engine


engine = create_engine("sqlite:///employees.db", echo=True)
Session = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


def create_db():
    Base.metadata.create_all(engine)


def drop_all():
    Base.metadata.drop_all(engine)
