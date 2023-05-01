#!/usr/bin/env python3
'''Password Encryption'''
import bcrypt


def hash_password(password: str) -> bytes:
    '''Hash password'''
    hack = bcrypt.gensalt()
    hashed_pw = bcrypt.hashpw(password.encode('utf-8'), hack)
    return hashed_pw


def is_valid(hashed_password: bytes, password: str) -> bool:
    '''Validate password'''
    check = bcrypt.checkpw(password.encode('utf-8'), hashed_password)
    return (check)
