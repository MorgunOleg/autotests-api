from pydantic import Field, EmailStr

from tools.assertions.schema import CamelModel
from tools.fakers import fake


class UserSchema(CamelModel):
    """
    Описание структуры пользователя.
    """
    id: str
    email: EmailStr
    last_name: str
    first_name: str
    middle_name: str


class CreateUserRequestSchema(CamelModel):
    """
    Описание структуры запроса на создание пользователя.
    """
    email: EmailStr = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)
    last_name: str = Field(default_factory=fake.last_name)
    first_name: str = Field(default_factory=fake.first_name)
    middle_name: str = Field(default_factory=fake.middle_name)


class CreateUserResponseSchema(CamelModel):
    """
    Описание структуры ответа создания пользователя.
    """
    user: UserSchema


class UpdateUserRequestSchema(CamelModel):
    """
    Описание структуры запроса на обновление пользователя.
    """
    email: EmailStr | None = Field(default_factory=fake.email)
    last_name: str | None = Field(default_factory=fake.last_name)
    first_name: str | None = Field(default_factory=fake.first_name)
    middle_name: str | None = Field(default_factory=fake.middle_name)


class UpdateUserResponseSchema(CamelModel):
    """
    Описание структуры ответа обновления пользователя.
    """
    user: UserSchema


class GetUserResponseSchema(CamelModel):
    """
    Описание структуры запроса получения пользователя.
    """
    user: UserSchema
