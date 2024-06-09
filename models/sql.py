import sqlite3
from db import db_session
from db.product import Product
from db.tags import Tags
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


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
            ans = db_sess.query(Product).all()
            return ans
        except Exception as e:
            print("(get_products_all):", e)
            return []

    def get_product(self, *args):
        try:
            db_sess = self.db_session.create_session()
            ans = self.get_products_all()
            res = set()

            for i in args:
                for j in ans:
                    tag = db_sess.query(Tags).filter(Tags.id == j.tag_id).first()
                    print(similar(i, j.name), similar(i, tag.name))
                    if similar(i, j.name) > 0.55 or similar(i, tag.name) > 0.65:
                        res.add(j)
            return res
        except Exception as e:
            print("(get_product):", e)
            return []
