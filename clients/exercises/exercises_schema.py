from pydantic import Field

from tools.assertions.schema import CamelModel
from tools.fakers import fake


class ExerciseSchema(CamelModel):
    """
    Описание структуры задания.
    """
    id: str
    title: str
    course_id: str
    max_score: int
    min_score: int
    order_index: int
    description: str
    estimated_time: str


class GetExerciseResponseSchema(CamelModel):
    """
    Описание структуры ответа на получение задания.
    """
    exercise: ExerciseSchema


class GetExercisesQuerySchema(CamelModel):
    """
    Описание структуры запроса на получение списка заданий определенного курса.
    """
    course_id: str


class GetExercisesResponseSchema(CamelModel):
    """
    Описание структуры ответа на получение списка заданий.
    """
    exercises: list[ExerciseSchema]


class CreateExerciseRequestSchema(CamelModel):
    """
    Описание структуры запроса на создание задания.
    """
    title: str = Field(default_factory=fake.sentence)
    course_id: str = Field(default_factory=fake.uuid4)
    max_score: int | None = Field(default_factory=fake.max_score)
    min_score: int | None = Field(default_factory=fake.min_score)
    order_index: int = Field(default_factory=fake.integer)
    description: str = Field(default_factory=fake.text)
    estimated_time: str | None = Field(default_factory=fake.estimated_time)


class CreateExerciseResponseSchema(CamelModel):
    """
    Описание структуры ответа создания задания.
    """
    exercise: ExerciseSchema


class UpdateExerciseRequestSchema(CamelModel):
    """
    Описание структуры запроса на обновление данных задания.
    """
    title: str | None = Field(default_factory=fake.sentence)
    max_score: int | None = Field(default_factory=fake.max_score)
    min_score: int | None = Field(default_factory=fake.min_score)
    order_index: int | None = Field(default_factory=fake.integer)
    description: str | None = Field(default_factory=fake.text)
    estimated_time: str | None = Field(default_factory=fake.estimated_time)


class UpdateExerciseResponseSchema(CamelModel):
    """
    Описание структуры ответа обновления задания.
    """
    exercise: ExerciseSchema
