#!/usr/bin/python3
"""Module defines a FileStorage instance - storage.

It then reloads instances on file from the storage instance.
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()

storage.reload()
