from fastapi_users import schemas
from fastapi_users.db.base import BaseUserDatabase


class User(schemas.BaseUser):
    '''Cхема с базовыми полями модели пользователя (за исключением пароля).'''
    pass


class UserCreate(schemas.BaseUserCreate):
    '''Cхема для регистрации пользователя; в неё обязательно
    должны быть переданы email и password.
    '''
    pass


class UserUpdate(schemas.BaseUserUpdate):
    '''Cхема для обновления объекта пользователя; содержит все базовые поля модели
    (в том числе и пароль). Все поля опциональны.
    '''
    pass


class UserDB(User, BaseUserDatabase):
    '''Cхема, описывающая модель в БД; пароль хранится в захэшированном
    виде в поле hashed_password.
    '''
    pass
