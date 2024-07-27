import os

from dotenv import load_dotenv

from ui_tests.src.enums.py_enum import PyEnum

load_dotenv()


class UserConfig(PyEnum):
    """
    Класс с данными пользователя
    """

    USER_LOGIN: str = os.environ.get('USER_LOGIN')
    USER_PASSWORD: str = os.environ.get('USER_PASSWORD')
