from http import HTTPStatus

import pytest

from clients.authentication.authentication_client import get_authentication_client
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema


@pytest.mark.regression
@pytest.mark.authentication
def test_login():
    # Инициализируем API-клиент для работы с пользователями
    public_users_client = get_public_users_client()

    # Инициализируем запрос на создание пользователя
    create_user_request = CreateUserRequestSchema()
    # Отправляем POST запрос на создание пользователя
    public_users_client.create_user(create_user_request)

    # Инициализируем API-клиент для аутентификации пользователя
    authentication_user_client = get_authentication_client()

    # Инициализируем запрос на аутентификацию
    login_request = LoginRequestSchema(
        email=str(create_user_request.email),
        password=create_user_request.password
    )
    # Выполняем POST запрос и аутентифицируемся
    login_response = authentication_user_client.login_api(login_request)

    # Инициализируем модель ответа на основе полученного JSON в ответе.
    # Проверяем корректность ответа по встроенной валидации Pydantic
    login_response_data = LoginResponseSchema.model_validate_json(login_response.text)

    # Проверяем статус-код ответа (200)
    assert_status_code(login_response.status_code, HTTPStatus.OK)

    # Проверяем корректность тела ответа
    assert_login_response(login_response_data)

    # Проверяем, что тело ответа соответствует ожидаемой JSON-схеме
    validate_json_schema(login_response.json(), login_response_data.model_json_schema())
