from http import HTTPStatus

import pytest

from clients.authentication.authentication_client import AuthenticationClient
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from clients.users.public_users_client import PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema
from tests.conftest import UserFixture
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema


@pytest.mark.regression
@pytest.mark.authentication
def test_login(function_user: UserFixture, authentication_client: AuthenticationClient):
    # Инициализируем запрос на аутентификацию
    request = LoginRequestSchema(email=str(function_user.email), password=function_user.password)
    # Выполняем POST запрос и аутентифицируемся
    response = authentication_client.login_api(request)

    # Инициализируем модель ответа на основе полученного JSON в ответе.
    # Проверяем корректность ответа по встроенной валидации Pydantic
    response_data = LoginResponseSchema.model_validate_json(response.text)

    # Проверяем статус-код ответа (200)
    assert_status_code(response.status_code, HTTPStatus.OK)

    # Проверяем корректность тела ответа
    assert_login_response(response_data)

    # Проверяем, что тело ответа соответствует ожидаемой JSON-схеме
    validate_json_schema(response.json(), response_data.model_json_schema())
