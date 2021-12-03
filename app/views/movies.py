from fastapi import APIRouter, status, Response
from app.implemented import movie_service
from app.dao.model.movies import MovieBM, MovieUpdateBM

router = APIRouter(prefix='/movies', tags=['movies'])


@router.get('', summary='Получить все фильмы')
async def movies_get_all():
    """
    Получить все фильмы
    """
    return movie_service.get_all()


@router.get('/{pk}', summary='Получить фильм по ID')
async def movies_get_one(pk: int):
    """
    Получить фильм по ID:

    - **pk**: ID фильма
    """
    return movie_service.get_one(pk)


@router.post('', status_code=status.HTTP_201_CREATED, summary='Добавить фильм',
             response_description="The created item")
async def movies_post(movie: MovieBM, response: Response):
    """
    Добавить фильм:

    - **id**: ID фильма - целое число (необязательный параметр)
    - **title**: название фильма (обязательный параметр)
    - **description**: описание фильма (обязательный параметр)
    - **rating**: рейтинг фильма
    - **director_id**: режиссер фильма (обязательный параметр)
    - **genre_id**: жанр фильма (обязательный параметр)
    - **year**: год выпуска фильма (обязательный параметр)
    - **trailer**: ссылка на трейлер (необязательный параметр)
    """
    new_obj = movie_service.create(movie.dict())
    response.headers['Location'] = f'{router.prefix}/{new_obj.id}'
    return []


@router.patch('/{pk}',
              # status_code=status.HTTP_204_NO_CONTENT,
              summary='Изменить запись о фильме с указанным ID')
async def movies_update(movie: MovieUpdateBM, pk: int):
    """
    Изменить запись о фильме с указанным ID:

    - **title**: название фильма
    - **description**: описание фильма
    - **rating**: рейтинг фильма
    - **director_id**: режиссер фильма
    - **genre_id**: жанр фильма
    - **year**: год выпуска фильма
    - **trailer**: ссылка на трейлер
    """
    return movie_service.update(movie.dict(), pk)


@router.delete('/{pk}', status_code=status.HTTP_200_OK, summary='Удалить запись о фильме с указанным ID')
async def movies_delete(pk: int):
    """
    Удалить запись о фильме с указанным ID:
    """
    movie_service.delete(pk)
    # return None
