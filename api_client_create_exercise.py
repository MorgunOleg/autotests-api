from clients.courses.courses_client import get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema
from clients.exercises.exercises_client import get_exercises_client
from clients.exercises.exercises_schema import (
    GetExercisesQuerySchema,
    CreateExerciseRequestSchema,
    UpdateExerciseRequestSchema
)
from clients.files.files_client import get_files_client
from clients.files.files_schema import CreateFileRequestSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema

public_users_client = get_public_users_client()

# Создаем пользователя
create_user_request = CreateUserRequestSchema()
create_user_response = public_users_client.create_user(create_user_request)

# Инициализируем клиенты на создание файлов и курсов
authentication_user = AuthenticationUserSchema(
    email=str(create_user_request.email),
    password=create_user_request.password
)
files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)

# Загружаем файл
create_file_request = CreateFileRequestSchema(upload_file="./testdata/files/image.png")
create_file_response = files_client.create_file(create_file_request)
print('Create file data:', create_file_response)

# Создаем курс
create_course_request = CreateCourseRequestSchema(
    preview_file_id=create_file_response.file.id,
    created_by_user_id=create_user_response.user.id
)
create_course_response = courses_client.create_course(create_course_request)
print('Create course data:', create_course_response)

# Создаем задание
exercises_client = get_exercises_client(authentication_user)
create_exercise_request = CreateExerciseRequestSchema()
create_exercise_response = exercises_client.create_exercise(create_exercise_request)
print('Create exercise data:', create_exercise_response)

# Получение списка заданий (тестовое)
get_exercises_request = GetExercisesQuerySchema(
    course_id=create_course_response.course.id
)
get_exercises_response = exercises_client.get_exercises(get_exercises_request)
print('Get exercises list:', get_exercises_response.exercises)

# Получение информации о задании (тестовое)
exercise_id = create_exercise_response.exercise.id
get_exercise_response = exercises_client.get_exercise(exercise_id)
print('Get exercise data:', get_exercise_response)

# Обновление задания (тестовое)
update_exercise_request = UpdateExerciseRequestSchema(
    title="Exercise 1.1",
    description="Updated exercise 1"
)
update_exercise_response = exercises_client.update_exercise(
    exercise_id,
    update_exercise_request
)
print('Update exercise data:', update_exercise_response)
