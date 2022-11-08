from fastapi import APIRouter

from apps.database.session import SQLITE

router = APIRouter(prefix='/v1/users')


@router.get('')
async def get_users():
    res = []
    users = await SQLITE.find('''
        SELECT id, email FROM user;
    ''')
    for user in users:
        id = user[0]
        email = user[1]
        res.append({'id': id, 'email': email})
    return {'users': res}
