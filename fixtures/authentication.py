import pytest

# Импортируем API клиент
from clients.authentication.authentication_client import AuthenticationClient, get_authentication_client


@pytest.fixture
def authentication_client() -> AuthenticationClient:
    # Создаем новый API клиент для работы с аутентификацией
    return get_authentication_client()
