#!/usr/bin/env python3
'''Authy'''
import bcrypt
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    '''Hash password and return byte'''

    salt = bcrypt.gensalt()

    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        '''Register User class'''
        exist = self._db.find_user_by(email=email)
        if exist:
            raise ValueError(f'User {email} already exists')

        hashed_password = _hash_password(password)
        user = User(email=email, hashed_password=hashed_password)
        self._db._session.add(user)
        self._db._session.commit()
        return user
