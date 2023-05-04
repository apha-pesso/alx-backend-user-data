#!/usr/bin/env python3
'''Auth class'''

from os import getenv
from flask import request
from typing import List, TypeVar


class Auth():
    '''Auth class'''

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''require auth'''
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        for excluded_path in excluded_paths:
            if path.rstrip('/').startswith(excluded_path.rstrip('/')):
                return False
        return True
        # if not path or excluded_paths is None:
        # return True

    '''
        for p in excluded_paths:
            if path == p:
                return False
            else:
                return True
        for excluded_path in excluded_paths:
            if path.rstrip('/').startswith(excluded_path.rstrip('/')):
                return False

        # if path in excluded_paths:
            return False

        # return False
    '''

    def authorization_header(self, request=None) -> str:
        '''Authorization Header'''
        # if request is None or request.headers('Authorization') is None:
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        '''Current user'''
        return None

    def session_cookie(self, request=None):
        '''Cookie session'''
        if not request:
            return None

        session_id = getenv("SESSION_NAME")
        return request.cookies.get(session_id)
