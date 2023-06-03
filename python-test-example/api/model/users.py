# -*- coding: utf-8 -*-
from database import Base
from sqlalchemy import INT, VARCHAR, Column
from sqlalchemy.orm import Session


class Users(Base):
    __tablename__ = 'users'

    id = Column('id', INT, primary_key=True, nullable=False,
                autoincrement=True, unique=True)
    name = Column('name', VARCHAR(191), nullable=False)

    def __init__(self, name):
        self.name = name

    def __str__(self):
        values = [item for item in vars(self).copy().items()][1:]
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s=%s' % item for item in values)
        )

    @staticmethod
    def find_all(session: Session):
        return session.query(Users).order_by(Users.id).all()
