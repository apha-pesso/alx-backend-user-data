#!/usr/bin/env python3
'''Authy'''
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4


def _hash_password(password: str) -> bytes:
    '''Hash password and return byte'''

    salt = bcrypt.gensalt()

    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed


def _generate_uuid() -> str:
    '''generate and return a uuid string'''
    new_id = str(uuid4())
    return new_id


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Create a new User by given Email and password
            if user exists with a given email return:
                User <user's email> already exists

        """
        # checking if user with email exists
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError('User {} already exists'.format(email))
        except NoResultFound:
            # hashed the password

            hashed_password = _hash_password(password)
            new_user = self._db.add_user(email, hashed_password)
            return new_user

    def valid_login(self, email: str, password: str) -> bool:
        '''Validate User password'''
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False

        hashed_pw = user.hashed_password
        input_byte = password.encode('utf-8')

        return bcrypt.checkpw(input_byte, hashed_pw)
