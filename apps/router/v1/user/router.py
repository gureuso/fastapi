import random
from fastapi import APIRouter

from apps.database import UserEntity
from apps.resp import UserListResp, UserResp
from apps.service.user import UserService

router = APIRouter(prefix='/v1/users')


@router.get('', response_model=UserListResp)
async def get_users():
    users = await UserService.find_all()
    return {'users': users}


@router.post('', response_model=UserResp)
async def create_user():
    user_entity = UserEntity(email=f'{random.randint(1000, 2000)}@gmail.com')
    user = await UserService.create(user_entity)
    return {'user': user}


@router.get('/{user_id}', response_model=UserResp)
async def get_user(user_id: int):
    user = await UserService.find_one_by_id(user_id)
    return {'user': user}
