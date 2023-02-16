#!/usr/bin/env python3
"""hashing"""
import bcrypt

def _hash_password(password:str) -> str: 
    """ returns bytes that is salted hash of 
        input password
    """
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed 
