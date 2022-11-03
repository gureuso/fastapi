from fastapi.requests import Request

from config import Config


class PermissionDeniedException(Exception):
    pass


class NotFoundException(Exception):
    pass


def error(code, message=None):
    if not message:
        message = Config.ERROR_CODE[code]

    result = {
        'code': code,
        'message': message
    }
    return result


async def verify_api_token(request: Request):
    token = request.cookies.get('token')
    current_user = token
    if not current_user:
        raise PermissionDeniedException()
    return current_user
