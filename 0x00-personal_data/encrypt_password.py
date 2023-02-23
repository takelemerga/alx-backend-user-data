#!/usr/bin/env python3
""" encripting password module """
import bcrypt


def hash_password(password: str) -> bytes:
    """encript password"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """validate"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
