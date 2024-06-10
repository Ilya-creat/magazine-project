import sqlalchemy
from .db_session import SqlAlchemyBase


class Payments(SqlAlchemyBase):
    __tablename__ = 'payments'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    uuid = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    name = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    number = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    address = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    order = sqlalchemy.Column(sqlalchemy.JSON, nullable=True)
    status = sqlalchemy.Column(sqlalchemy.BOOLEAN, nullable=True)
