import os
import databases
import sqlalchemy
from pydantic import BaseModel

from config import Config

DATABASE_URL = f'''sqlite:///{os.path.join(Config.ROOT_DIR, 'prod.db')}'''
TEST_DATABASE_URL = f'''sqlite:///{os.path.join(Config.ROOT_DIR, 'test.db')}'''
database = databases.Database(TEST_DATABASE_URL if Config.is_test() else DATABASE_URL)

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
test_engine = sqlalchemy.create_engine(
    TEST_DATABASE_URL, connect_args={'check_same_thread': False}
)
metadata.create_all(engine)
metadata.drop_all(test_engine)
metadata.create_all(test_engine)


class UserEntity(BaseModel):
    id: int | None = None
    email: str
