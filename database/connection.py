import os
import sqlite3


class WordStorageConnection(sqlite3.Connection):
    """
    Creates a Connection object to the word_storage database.
    """

    def __init__(self) -> None:
        db_dir = os.path.dirname(__file__)
        db_abs_path = os.path.join(db_dir, "word_storage.db")
        super().__init__(db_abs_path)
