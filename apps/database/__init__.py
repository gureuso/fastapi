import os
import databases
import sqlalchemy
from pydantic import BaseModel

from config import Config

DATABASE_URL = f'''sqlite:///{os.path.join(Config.ROOT_DIR, 'fastapi.db')}'''
database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()
user_table = sqlalchemy.Table(
    'user',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('email', sqlalchemy.String, unique=True),
)
engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={'check_same_thread': False}
)
# metadata.create_all(engine)


class UserEntity(BaseModel):
    id: int
    email: str
