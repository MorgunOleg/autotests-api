from pydantic import Field
from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema
from tools.assertions.schema import CamelModel
from tools.fakers import fake


class CourseSchema(CamelModel):
    """
    Описание структуры курса.
    """
    id: str
    title: str
    max_score: int
    min_score: int
    description: str
    preview_file: FileSchema
    estimated_time: str
    created_by_user: UserSchema


class GetCoursesQuerySchema(CamelModel):
    """
    Описание структуры запроса на получение списка курсов.
    """
    user_id: str


class CreateCourseRequestSchema(CamelModel):
    """
    Описание структуры запроса на создание курса.
    """
    title: str = Field(default_factory=fake.sentence)
    max_score: int = Field(default_factory=fake.max_score)
    min_score: int = Field(default_factory=fake.min_score)
    description: str = Field(default_factory=fake.text)
    estimated_time: str = Field(default_factory=fake.estimated_time)
    preview_file_id: str = Field(default_factory=fake.uuid4)
    created_by_user_id: str = Field(default_factory=fake.uuid4)


class CreateCourseResponseSchema(CamelModel):
    """
    Описание структуры ответа создания курса.
    """
    course: CourseSchema


class UpdateCourseRequestSchema(CamelModel):
    """
    Описание структуры запроса на обновление курса.
    """
    title: str | None = Field(default_factory=fake.sentence)
    max_score: int | None = Field(default_factory=fake.max_score)
    min_score: int | None = Field(default_factory=fake.min_score)
    description: str | None = Field(default_factory=fake.text)
    estimated_time: str | None = Field(default_factory=fake.estimated_time)
