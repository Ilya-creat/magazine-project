import sqlite3
from db import db_session
from db.__all_models import product


class DataBase:
    def __init__(self, db):
        if type(db) != sqlite3.Connection:
            self.__db = sqlite3.Connection(db, check_same_thread=False)

            self.__cur = self.__db.cursor()

        self.db_session = db_session
        self.db_session.global_init(db)

    def get_products_all(self):
        try:
            db_sess = self.db_session.create_session()
            ans = db_sess.query(product.Product).all()
            return ans
        except Exception as e:
            print("(get_products_all):", e)
