#!/usr/bin/env python3
'''Basic Auth class'''

from api.v1.auth.auth import Auth
import base64


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
