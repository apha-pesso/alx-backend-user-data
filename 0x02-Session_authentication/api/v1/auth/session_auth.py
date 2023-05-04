#!/usr/bin/env python3
'''Session Auth class'''

from api.v1.auth.auth import Auth
# from models.user import User
# from typing import TypeVar


class SessionAuth(Auth):
    '''Session Auth class'''
    user_id_by_session_id = {}
    pass
