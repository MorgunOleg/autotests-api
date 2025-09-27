from pydantic import Field

from tools.assertions.schema import CamelModel
from tools.fakers import fake


class TokenSchema(CamelModel):
    """
    Описание структуры аутентификационных токенов.
    """
    token_type: str
    access_token: str
    refresh_token: str


class LoginRequestSchema(CamelModel):
    """
    Описание структуры запроса на аутентификацию.
    """
    email: str = Field(default_factory=fake.email())
    password: str = Field(default_factory=fake.password())


class LoginResponseSchema(CamelModel):
    """
    Описание структуры ответа аутентификации.
    """
    token: TokenSchema


class RefreshRequestSchema(CamelModel):
    """
    Описание структуры запроса для обновления токена.
    """
    refresh_token: str = Field(default_factory=fake.sentence())
