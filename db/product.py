import sqlalchemy
from .db_session import SqlAlchemyBase


class Product(SqlAlchemyBase):
    __tablename__ = 'products'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    info = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    tag_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    picture = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    price = sqlalchemy.Column(sqlalchemy.Float, nullable=True)
    count = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)