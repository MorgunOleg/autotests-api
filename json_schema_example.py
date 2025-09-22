from jsonschema import validate, ValidationError

# Примеры схем
schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "number"}
    },
    "required": ["name"]
}

schema2 = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "value": {"type": "number"}
        },
        "required": ["id", "value"]
    }
}

schema3 = {
    "type": "object",
    "properties": {
        "username": {
            "type": "string",
            "minLength": 3,
            "maxLength": 20
        }
    },
    "required": ["username"]
}

schema4 = {
    "type": "object",
    "properties": {
        "email": {
            "type": "string",
            "pattern": "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$"
        }
    },
    "required": ["email"]
}

# Пример данных
data = {
    "name": "John Doe",
    "age": 30
}

try:
    validate(instance=data, schema=schema)
    print("Данные соответствуют схеме.")
except ValidationError as e:
    print(f"Ошибка валидации: {e.message}")
