from typing import Any

import allure
from jsonschema import validate
from jsonschema.validators import Draft202012Validator

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel

from tools.logger import get_logger

logger = get_logger("SCHEMA_ASSERTIONS")  # Создаем логгер с именем "SCHEMA_ASSERTIONS"


class CamelModel(BaseModel):
    """
    Базовый класс для Pydantic моделей с поддержкой camelCase alias.
    """
    model_config = ConfigDict(
        alias_generator=to_camel,
        validate_by_name=True,
        serialize_by_alias=True
    )


@allure.step("Validate JSON schema")
def validate_json_schema(instance: Any, schema: dict) -> None:
    """
    Проверяет, соответствует ли JSON-объект (instance) заданной JSON-схеме (schema).

    :param instance: JSON-данные, которые нужно проверить.
    :param schema: Ожидаемая JSON-schema.
    :raises jsonschema.exceptions.ValidationError: Если instance не соответствует schema.
    """
    logger.info("Validating JSON schema")

    validate(
        schema=schema,
        instance=instance,
        format_checker=Draft202012Validator.FORMAT_CHECKER,
    )
