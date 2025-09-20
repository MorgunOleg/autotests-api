from pydantic import BaseModel, ConfigDict, Field
# from pydantic.alias_generators import to_camel
#
#
# class CamelModel(BaseModel):
#     """
#     Базовый класс для Pydantic моделей с поддержкой camelCase alias.
#     """
#     model_config = ConfigDict(
#         alias_generator=to_camel,
#         validate_by_name=True,
#         serialize_by_alias=True
#     )


class TokenSchema(BaseModel):
    """
    Описание структуры аутентификационных токенов.
    """
    token_type: str = Field(alias="tokenType")
    access_token: str = Field(alias="accessToken")
    refresh_token: str = Field(alias="refreshToken")


class LoginRequestSchema(BaseModel):
    """
    Описание структуры запроса на аутентификацию.
    """
    email: str
    password: str


class LoginResponseSchema(BaseModel):
    """
    Описание структуры ответа аутентификации.
    """
    token: TokenSchema


class RefreshRequestSchema(BaseModel):
    """
    Описание структуры запроса для обновления токена.
    """
    refresh_token: str = Field(alias="refreshToken")
