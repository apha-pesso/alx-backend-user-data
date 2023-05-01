#!/usr/bin/env python3
'''Password Encryption'''
import bcrypt


def hash_password(password: str) -> bytes:
    '''Hash password'''
    hack = bcrypt.gensalt()
    hashed_pw = bcrypt.hashpw(password.encode('utf-8'), hack)
    return hashed_pw
