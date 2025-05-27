from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict


class CetExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка курсов.
    """
    courseId: str


class CreateExercisesRequestDict(TypedDict):
    """
    Описание структуры запроса на создание exercises.
    """
    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str


class UpdateExercisesRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление exercises.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """
    def get_exercises_api(self, query)  ->Response:
        """
        Метод получения списка курсов.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get('/api/v1/exercises', params=query)


    def get_exercise_api(self, exercises_id: str) -> Response:
        """
        Метод получения exercises.

        :param exercises_id: Идентификатор exercises.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f'/api/v1/exercises/{exercises_id}')

    def create_exercise_api(self, request: CreateExercisesRequestDict) -> Response:
        """
        Метод создания exercises.

        :param request: Словарь с title, maxScore, minScore, description, estimatedTime,
        previewFileId, createdByUserId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request)


    def update_exercise_api(self, exercises_id, request: UpdateExercisesRequestDict) -> Response:
        """
        Метод обновления курса.

        :param exercises_id: Идентификатор курса.
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.path(f"/api/v1/exercises/{exercises_id}", json=request)

    def delete_exercise_api(self, exercises_id) -> Response:
        """
        Метод удаления курса.

        :param exercises_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f'/api/v1/exercises/{exercises_id}')