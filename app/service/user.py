from app.database import user_table, database, UserEntity


class UserService:
    @staticmethod
    async def create(user_entity: UserEntity):
        query = user_table.insert().values(email=user_entity.email)
        user_entity.id = await database.execute(query)
        return user_entity

    @staticmethod
    async def find_all():
        query = user_table.select()
        return await database.fetch_all(query)

    @staticmethod
    async def find_one_by_id(user_id: int):
        query = user_table.select().where(user_table.c.id == user_id)
        return await database.fetch_one(query)
