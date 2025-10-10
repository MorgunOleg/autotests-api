import pytest

from pydantic import BaseModel, EmailStr

# Импортируем API клиенты
from clients.authentication.authentication_client import get_authentication_client, AuthenticationClient
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client, PrivateUsersClient
from clients.users.public_users_client import get_public_users_client, PublicUsersClient
# Импортируем запрос и ответ создания пользователя, модель данных пользователя
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema


# Модель для агрегации возвращаемых данных фикстурой function_user
class UserFixture(BaseModel):
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema

    @property
    def email(self) -> EmailStr:
        return self.request.email

    @property
    def password(self) -> str:
        return self.request.password

    @property
    def authentication_user(self) -> AuthenticationUserSchema:
        return AuthenticationUserSchema(email=self.email, password=self.password)


@pytest.fixture
def authentication_client() -> AuthenticationClient:
    # Создаем новый API клиент для работы с аутентификацией
    return get_authentication_client()


@pytest.fixture
def public_users_client() -> PublicUsersClient:
    # Создаем новый API клиент для работы с публичным API пользователей
    return get_public_users_client()


@pytest.fixture
def function_user(public_users_client: PublicUsersClient) -> UserFixture:
    # Инициализируем запрос на создание пользователя
    request = CreateUserRequestSchema()
    # Отправляем POST запрос на создание пользователя
    response = public_users_client.create_user(request)
    return UserFixture(request=request, response=response)


@pytest.fixture
def private_users_client(function_user: UserFixture) -> PrivateUsersClient:
    # Создаем новый инициализированный API клиент для работы с /api/v1/users
    return get_private_users_client(function_user.authentication_user)
