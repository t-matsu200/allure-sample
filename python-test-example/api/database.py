# -*- coding: utf-8 -*-
import os
import tempfile

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker

Base = declarative_base()


class SqliteDatabase:
    """動作確認用"""

    def __init__(self):
        self.SQLALCHEMY_DATABASE_URL = 'sqlite:////db/sample_db.sqlite3'
        self.engine = create_engine(
            self.SQLALCHEMY_DATABASE_URL,
            connect_args={'encoding': 'utf-8'}
        )
        self.SessionLocal = scoped_session(
            sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        )
        self.Base = Base
        self.Base.query = self.SessionLocal.query_property()

    def get_db(self):
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()

    def create_tables(self):
        self.Base.metadata.create_all(bind=self.engine)


class Database:
    def __init__(self, db_type: str, username: str, password: str, host: str, port: str, db_name: str):
        self.SQLALCHEMY_DATABASE_URL = f'{db_type}://{username}:{password}@{host}:{port}/{db_name}?charset=utf8'
        self.engine = create_engine(
            self.SQLALCHEMY_DATABASE_URL,
            connect_args={'encoding': 'utf-8'},
            pool_size=20,
            max_overflow=15,
            pool_timeout=5,
            pool_recycle=3600,
            pool_pre_ping=True
        )
        self.SessionLocal = scoped_session(
            sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        )
        self.Base = Base
        self.Base.query = self.SessionLocal.query_property()

    def get_db(self):
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()

    def create_tables(self):
        self.Base.metadata.create_all(bind=self.engine)


class TestDatabase:
    def __init__(self):
        # for unit test
        sql_file = os.path.join(tempfile.mkdtemp(), 'test_fastapi.sqlite3')
        self.SQLALCHEMY_DATABASE_URL = 'sqlite:///' + sql_file
        self.engine = create_engine(
            self.SQLALCHEMY_DATABASE_URL
        )
        self.SessionLocal = scoped_session(
            sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        )
        self.Base = Base
        self.Base.query = self.SessionLocal.query_property()

    def get_db(self):
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()

    def setup_database(self):
        session = self.SessionLocal()
        try:
            self.Base.metadata.create_all(bind=self.engine)
            tables = self.Base.metadata.tables
            table = tables.get('users')
            session.execute(table.insert().values(id=0, name='test-user'))
            session.commit()
        finally:
            session.close()
