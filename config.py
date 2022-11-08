# -*- coding: utf-8 -*-
import os
import json


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


class JsonConfig:
    DATA = json.loads(open('{}/config.json'.format(ROOT_DIR)).read())

    @staticmethod
    def get_data(varname, value=None):
        result = JsonConfig.DATA.get(varname) or os.getenv(varname) or value
        if result == 'true':
            return True
        elif result == 'false':
            return False
        return result

    @staticmethod
    def set_data(key, value):
        JsonConfig.DATA[key] = value
        with open('{}/config.json'.format(ROOT_DIR), 'w') as f:
            json.dump(JsonConfig.DATA, f, indent=4)


# app config
class Config:
    ROOT_DIR = ROOT_DIR
    STATIC_DIR = '{0}/static'.format(ROOT_DIR)
    TEMPLATES_DIR = '{0}/template'.format(ROOT_DIR)
    ERROR_CODE = {
        40000: '입력 값이 잘못되었습니다.',
        40300: '권한이 없습니다.',
        40400: '찾을 수 없습니다.',
        50000: '서버 에러. 관리자에게 문의하세요.',
    }

    APP_MODE_PRODUCTION = 'production'
    APP_MODE_DEVELOPMENT = 'development'
    APP_MODE_TESTING = 'testing'

    APP_MODE = JsonConfig.get_data('APP_MODE', APP_MODE_DEVELOPMENT)
    APP_HOST = JsonConfig.get_data('APP_HOST', '0.0.0.0')
    APP_PORT = int(JsonConfig.get_data('APP_PORT', 8000))

    DB_USER_NAME = JsonConfig.get_data('DB_USER_NAME', 'root')
    DB_USER_PASSWD = JsonConfig.get_data('DB_USER_PASSWD', 'asdf1234')
    DB_HOST = JsonConfig.get_data('DB_HOST', 'gureuso.me')
    DB_NAME = JsonConfig.get_data('DB_NAME', 'fastapi')

    REDIS_HOST = JsonConfig.get_data('REDIS_HOST', 'localhost')
    REDIS_PASSWD = JsonConfig.get_data('REDIS_PASSWD', None)

    @staticmethod
    def is_production():
        if Config.APP_MODE == Config.APP_MODE_PRODUCTION:
            return True
        return False

    @staticmethod
    def database_url(dialect='mysql'):
        if dialect == 'mysqlconnector':
            return '{}://{}:{}@{}/{}?charset=utf8mb4'.format('mysql+mysqlconnector', Config.DB_USER_NAME, Config.DB_USER_PASSWD,
                                                          Config.DB_HOST, Config.DB_NAME)
        if dialect == 'mongodb':
            return '{}://{}:{}@{}'.format(dialect, Config.DB_USER_NAME, Config.DB_USER_PASSWD, Config.DB_HOST)

        return '{}://{}:{}@{}/{}?charset=utf8mb4'.format(dialect, Config.DB_USER_NAME, Config.DB_USER_PASSWD,
                                                      Config.DB_HOST, Config.DB_NAME)
