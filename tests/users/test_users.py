from http import HTTPStatus

import allure
import pytest
from allure_commons.types import Severity

from clients.users.private_users_client import PrivateUsersClient
from clients.users.public_users_client import PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from fixtures.users import function_user, UserFixture
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from tools.assertions.users import assert_create_user_response, assert_get_user_response
from tools.fakers import fake


@pytest.mark.users
@pytest.mark.regression
@allure.tag(AllureTag.USERS, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.USERS)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.USERS)
class TestUsers:
    @pytest.mark.parametrize("domain", ["mail.ru", "gmail.com", "example.com"])
    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.title("Create user")
    @allure.severity(Severity.BLOCKER)
    @allure.sub_suite(AllureStory.CREATE_ENTITY)
    def test_create_user(
            self,
            domain: str,
            public_users_client: PublicUsersClient
    ):
        # Формируем тело запроса на создание пользователя с параметризацией домена
        request = CreateUserRequestSchema(email=fake.email(domain))
        # Отправляем запрос на создание пользователя
        response = public_users_client.create_user_api(request)
        # Инициализируем модель ответа на основе полученного JSON в ответе.
        # Проверяем корректность ответа по встроенной валидации Pydantic
        response_data = CreateUserResponseSchema.model_validate_json(response.text)

        # Проверяем статус-код ответа
        assert_status_code(response.status_code, HTTPStatus.OK)
        # Проверяем, что данные ответа совпадают с данными запроса
        assert_create_user_response(request, response_data)

        # Проверяем, что тело ответа соответствует ожидаемой JSON-схеме
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag(AllureTag.GET_ENTITY)
    @allure.story(AllureStory.GET_ENTITY)
    @allure.title("Get user me")
    @allure.severity(Severity.CRITICAL)
    @allure.sub_suite(AllureStory.GET_ENTITY)
    def test_get_user_me(
            self,
            private_users_client: PrivateUsersClient,
            function_user: UserFixture
    ):
        # Отправляем запрос на получение данных пользователя
        response = private_users_client.get_user_me_api()

        # Проверяем статус-код ответа (200)
        assert_status_code(response.status_code, HTTPStatus.OK)

        # Валидируем тело ответа и проверяем на соответствие запросу по созданию пользователя
        response_data = GetUserResponseSchema.model_validate_json(response.text)
        assert_get_user_response(response_data, function_user.response)

        # Проверяем, что тело ответа соответствует ожидаемой JSON-схеме
        validate_json_schema(response.json(), response_data.model_json_schema())
