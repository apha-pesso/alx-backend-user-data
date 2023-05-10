#!/usr/bin/env python3
'''Authy'''
import bcrypt


def _hash_password(password: str) -> bytes:
    '''Hash password and return byte'''

    salt = bcrypt.gensalt()

    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed
