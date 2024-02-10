#!/usr/bin/python3
"""
Create FileStorage instance for the application
"""
from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
