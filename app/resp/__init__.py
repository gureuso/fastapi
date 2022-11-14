from pydantic.main import BaseModel

from app.database import UserEntity


class UserListResp(BaseModel):
    users: list[UserEntity]


class UserResp(BaseModel):
    user: UserEntity
