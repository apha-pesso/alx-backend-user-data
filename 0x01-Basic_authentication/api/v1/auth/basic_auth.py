#!/usr/bin/env python3
'''Basic Auth class'''

from api.v1.auth.auth import Auth
import base64
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    '''Basic Auth class'''

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        '''Extract Authorization header'''
        if not authorization_header or not isinstance(
                authorization_header,
                str) or not authorization_header.startswith('Basic'):
            return None
        authy = authorization_header.split()
        if len(authy) < 2:
            return None
        return authy[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        '''Decode base64 string'''
        if not base64_authorization_header or not isinstance(
                base64_authorization_header, str):
            return None

        try:
            decoded = base64.b64decode(base64_authorization_header)
            return decoded.decode('utf-8')
        except BaseException:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        '''Extract User credentials
            email:password
            split(:)
            return email and password
        '''
        if not decoded_base64_authorization_header or not isinstance(
                decoded_base64_authorization_header, str):
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)

        cred = decoded_base64_authorization_header.split(':')

        if len(cred) == 2:
            return (cred[0], cred[1])

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str) -> TypeVar('User'):
        '''Get user object'''
        if not user_email or not isinstance(user_email, str):
            return None
        if not user_pwd or not isinstance(user_pwd, str):
            return None
        try:
            user = User.search({'email': user_email})
        except Exception:
            return None

        if len(user) == 0:
            return None

        if user[0].is_valid_password(user_pwd):
            return user[0]
        else:
            return None
