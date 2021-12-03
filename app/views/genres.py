from fastapi import APIRouter, status, Response
from app.implemented import genre_service
from app.dao.model.genres import GenreBM, GenreUpdateBM

router = APIRouter(prefix='/genres', tags=['genres'])


@router.get('', summary='Получить все жанры')
async def genres_get_all():
    """
    Получить все жанры
    """
    return genre_service.get_all()


@router.get('/{pk}', summary='Получить жанр по его ID')
async def genres_get_one(pk: int):
    """
    Получить жанр по ID:

    - **pk**: ID жанра
    """
    return genre_service.get_one(pk)


@router.post('', status_code=status.HTTP_201_CREATED, summary='Добавить жанр',
             response_description="The created item")
async def genres_post(genre: GenreBM, response: Response):
    """
    Добавить жанр:

    - **id**: ID жанра - целое число (необязательный параметр)
    - **name**: название жанра (обязательный параметр)
    """
    new_obj = genre_service.create(genre.dict())
    response.headers['Location'] = f'{router.prefix}/{new_obj.id}'
    return []


@router.patch('/{pk}',
              # status_code=status.HTTP_204_NO_CONTENT,
              summary='Изменить запись о жанре с указанным ID')
async def genres_update(genre: GenreUpdateBM, pk: int):
    """
    Изменить запись о жанре с указанным ID:

    - **name**: изменить название жанра
    """
    return genre_service.update(genre.dict(), pk)


@router.delete('/{pk}', status_code=status.HTTP_200_OK, summary='Удалить запись о жанре с указанным ID')
async def genres_delete(pk: int):
    """
    Удалить запись о жанре с указанным ID:
    """
    genre_service.delete(pk)
    # return None
