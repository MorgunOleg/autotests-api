from pydantic import HttpUrl, Field

from tools.assertions.schema import CamelModel
from tools.fakers import fake


class FileSchema(CamelModel):
    """
    Описание структуры файла.
    """
    id: str
    url: HttpUrl
    filename: str
    directory: str


class CreateFileRequestSchema(CamelModel):
    """
    Описание структуры запроса на создание файла.
    """
    filename: str = Field(default_factory=lambda: f"{fake.uuid4()}.png")
    directory: str = Field(default="tests")
    upload_file: str


class CreateFileResponseSchema(CamelModel):
    """
    Описание структуры ответа создания файла.
    """
    file: FileSchema


class GetFileResponseSchema(CamelModel):
    """
    Описание структуры запроса получения файла.
    """
    file: FileSchema
