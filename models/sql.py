import sqlite3
from db import db_session
from db import __all_models


class DataBase:
    def __init__(self, db):
        if type(db) != sqlite3.Connection:
            self.__db = sqlite3.Connection(db, check_same_thread=False)

            self.__cur = self.__db.cursor()

        self.db_session = db_session
        self.db_session.global_init(db)
