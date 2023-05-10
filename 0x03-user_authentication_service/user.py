#!/usr/bin/env python3
'''
Create SQLAlchemy model named User with attributes
'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from typing import Optional

Base = declarative_base()

# create the user class


class User(Base):
    '''Creating the user table'''
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)

    def __init__(self, email: str, hashed_password: str,
                 session_id: Optional[str] = None,
                 reset_token: Optional[str] = None) -> None:
        '''Class constructor'''
        self.email = email
        self.hashed_password = hashed_password
        self.session_id = session_id
        self.reset_token = reset_token
