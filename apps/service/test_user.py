import uuid

import pytest

from apps.database import UserEntity
from apps.service.user import UserService


class TestUserService:
    @pytest.mark.asyncio
    async def test_find_all(self):
        users = await UserService.find_all()
        assert len(users) > -1

    @pytest.mark.asyncio
    async def test_find_one_by_id(self):
        user = await UserService.find_one_by_id(user_id=0)
        assert user is None

    @pytest.mark.asyncio
    async def test_create(self):
        user_entity = UserEntity(email=f'{uuid.uuid4()}@gmail.com')
        create_user = await UserService.create(user_entity)
        find_user = await UserService.find_one_by_id(user_id=create_user.id)
        assert create_user.id == find_user.id
