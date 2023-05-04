#!/usr/bin/env python3
'''Session Auth class'''

from api.v1.auth.auth import Auth
from uuid import uuid4
# from models.user import User
# from typing import TypeVar


class SessionAuth(Auth):
    '''Session Auth class'''
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        '''Create session id'''
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid4())
        user_id_by_session_id[session_id] = user_id
        return session_id
