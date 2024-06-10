import sqlalchemy
from .db_session import SqlAlchemyBase


class Tags(SqlAlchemyBase):
    __tablename__ = 'tags'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
