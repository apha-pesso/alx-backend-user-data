#!/usr/bin/env python3
'''Logging formater'''
from typing import List
import re
import logging

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str) -> str:
    '''Obfuscate log message'''

    for field in fields:
        # pattern = rf'{field}=([^;]+){separator}'
        # pattern = rf'({field}=)[a-zA-Z0-9]+{separator}'
        # pattern = rf'({field}=)[*+]{separator}'
        pattern = rf'(?<={field}=).*?(?={separator})'
        message = re.sub(pattern, redaction, message)
        # print(field)

    return message


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        '''initialize class'''
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        '''Format method'''
        record.msg = filter_datum(
            self.fields,
            self.REDACTION,
            record.msg,
            self.SEPARATOR)
        return super().format(record)


def get_logger() -> logging.Logger:
    '''User data logger'''
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    formatter = RedactingFormatter(list(PII_FIELDS))
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return (logger)
