#!/usr/bin/env python3
'''Session Auth class'''

from api.v1.auth.auth import Auth
from uuid import uuid4
from models.user import User
from typing import TypeVar


class SessionAuth(Auth):
    '''Session Auth class'''
    user_id_by_session_id = {}

    def __init__(self):
        '''Initializer'''
        super().__init__()

        # self.user_id_by_session_id = user_id_by_session_id

    def create_session(self, user_id: str = None) -> str:
        '''Create session id'''
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        '''Return user id'''
        if session_id is None or not isinstance(session_id, str):
            return None

        user_id = self.user_id_by_session_id.get(session_id)
        return user_id

    def current_user(self, request=None) -> TypeVar('User'):
        '''Return user object based on cookie'''
        # Get session ID
        session_id = self.session_cookie(request)

        # Get user_id with session_id
        user_id = self.user_id_for_session_id(session_id)

        # Retrieve User object with the user_id
        user = User.get(user_id)
        return user
