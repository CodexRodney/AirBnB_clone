#!/usr/bin/python3
"""
The __init__ file
"""

from models.engine import file_storage


storage = file_storage.FileStorage()
storage.reload()
