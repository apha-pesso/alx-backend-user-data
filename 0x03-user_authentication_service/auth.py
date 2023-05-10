#!/usr/bin/env python3
""""Password hashing
"""
from bcrypt import hashpw, gensalt
import bcrypt
import base64
from db import DB, User
from typing import Optional
from sqlalchemy.orm.exc import NoResultFound
from user import User
from uuid import uuid4


def _hash_password(self, password: str) -> bytes:
    """Returns encrypted password
    Args: password
    """
    # salt = bcrypt.gensalt()
    # encoded_password = password.encode('utf-8')
    # hashed_password = bcrypt.hashpw(encoded_password, salt)
    return hashpw(password.encode('utf-8'), gensalt())


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

            hashed_password = _hash_password(self, password)
            new_user = self._db.add_user(email, hashed_password)
            return new_user
