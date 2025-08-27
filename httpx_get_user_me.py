import httpx

login_payload = {
    "email": "raubtierm@gmail.com",
    "password": "Qwerty135"
}

# Проверка на успешное получение токена
try:
    login_response = httpx.post(
        "http://localhost:8000/api/v1/authentication/login", json=login_payload)
    login_response.raise_for_status()
    access_token = login_response.json()['token']['accessToken']
except httpx.HTTPStatusError as er:
    print(f"Ошибка запроса: {er}")
    raise

authorization_payload = {"Authorization": f"Bearer {access_token}"}
authorization_response = httpx.get(
    "http://localhost:8000/api/v1/users/me", headers=authorization_payload)

print(authorization_response.json())
print(authorization_response.status_code)
