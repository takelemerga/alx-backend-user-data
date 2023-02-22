#!/usr/bin/env python3
"""log message"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """returns log message obfuscated"""
    for field in fields:
        pattern = r'({0}=)[^{1}]*({1})'.format(field, separator)
        # print(pattern)
        log_message = re.sub(pattern, r'\1{}\2'.format(redaction), message)
    return log_message
