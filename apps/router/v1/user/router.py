from fastapi import APIRouter

from apps.resp import UserListResp, UserResp
from apps.service.user import UserService

router = APIRouter(prefix='/v1/users')


@router.get('', response_model=UserListResp)
async def get_users():
    users = await UserService.find_all()
    return {'users': users}


@router.get('/{user_id}', response_model=UserResp)
async def get_user(user_id: int):
    user = await UserService.find_one_by_id(user_id)
    return {'user': user}
