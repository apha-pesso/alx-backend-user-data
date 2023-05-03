#!/usr/bin/env python3
'''Basic Auth class'''

from api.v1.auth.auth import Auth


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
