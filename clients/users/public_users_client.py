from typing import TypedDict

import httpx

from clients.api_client import APIClient


class CreateUserDict(TypedDict):
    """
    Описание структуры запроса на создание нового пользователя
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(APIClient):
    """
    Клиент для работы с эндпоинтом /api/v1/users
    """

    def create_user_api(self, request: CreateUserDict) -> httpx.Response:
        """
        Метод выполняет создание нового пользователя.

        :param request: Словарь с параметрами нового пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/users", json=request)
