import httpx

# GET-запрос
response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")

print(response.status_code)  # 200
print(response.json())  # {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}

# POST-запрос
data = {
    "title": "Новая задача",
    "completed": False,
    "userId": 1
}

response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)

print(response.status_code)  # 201 (Created)
print(response.request.headers)
print(response.json())  # Ответ с созданной записью

# form-data запрос
data = {"username": "test_user", "password": "123456"}

response = httpx.post("https://httpbin.org/post", data=data)
print(response.request.headers)
print(response.json())  # {'form': {'username': 'test_user', 'password': '123456'}, ...}

# Передача заголовков
headers = {"Authorization": "Bearer my_secret_token"}

response = httpx.get("https://httpbin.org/get", headers=headers)
print(response.request.headers)
print(response.json())  # Заголовки включены в ответ

# Работа с параметрами запроса
params = {"userId": 1}

response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)

print(response.url)    # https://jsonplaceholder.typicode.com/todos?userId=1
print(response.json()) # Фильтрованный список задач

# Отправка файлов
files = {"file": ("example.txt", open("example.txt", "rb"))}

response = httpx.post("https://httpbin.org/post", files=files)
print(response.json())  # Ответ с данными о загруженном файле
files["file"][1].close()

# Использование httpx.Client
with httpx.Client() as client:
    response1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
    response2 = client.get("https://jsonplaceholder.typicode.com/todos/2")

print(response1.json())  # Данные первой задачи
print(response2.json())  # Данные второй задачи

client = httpx.Client(headers={"Authorization": "Bearer my_secret_token"})

response = client.get("https://httpbin.org/get")

print(response.json())  # Заголовки включены в ответ
client.close()

# Работа с ошибками (4xx, 5xx)
try:
    response = httpx.get("https://jsonplaceholder.typicode.com/invalid-url")
    response.raise_for_status()  # Вызовет исключение при 4xx/5xx
except httpx.HTTPStatusError as e:
    print(f"Ошибка запроса: {e}")

# Обработка таймаутов
try:
    response = httpx.get("https://httpbin.org/delay/5", timeout=None)
except httpx.ReadTimeout:
    print("Запрос превысил лимит времени")
