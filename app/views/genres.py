from fastapi import APIRouter, status, Response, Depends
from app.dao.model.genres import GenreBM, GenreUpdateBM
from app.service.genres import GenreService
from app.dependency import get_db
from sqlalchemy.orm import Session


router = APIRouter(prefix='/genres', tags=['genres'])


@router.get('', summary='Получить все жанры')
async def genres_get_all(db: Session = Depends(get_db)):
    """
    Получить все жанры
    """
    return GenreService(db).get_all()


@router.get('/{pk}', summary='Получить жанр по его ID')
async def genres_get_one(pk: int, db: Session = Depends(get_db)):
    """
    Получить жанр по ID:

    - **pk**: ID жанра
    """
    return GenreService(db).get_one(pk)


@router.post('', status_code=status.HTTP_201_CREATED, summary='Добавить жанр',
             response_description="The created item")
async def genres_post(genre: GenreBM, response: Response, db: Session = Depends(get_db)):
    """
    Добавить жанр:

    - **id**: ID жанра - целое число (необязательный параметр)
    - **name**: название жанра (обязательный параметр)
    """
    new_obj = GenreService(db).create(genre.dict())
    response.headers['Location'] = f'{router.prefix}/{new_obj.id}'
    return []


@router.patch('/{pk}',
              # status_code=status.HTTP_204_NO_CONTENT,
              summary='Изменить запись о жанре с указанным ID')
async def genres_update(genre: GenreUpdateBM, pk: int, db: Session = Depends(get_db)):
    """
    Изменить запись о жанре с указанным ID:

    - **name**: изменить название жанра
    """
    return GenreService(db).update(genre.dict(), pk)


@router.delete('/{pk}', status_code=status.HTTP_200_OK, summary='Удалить запись о жанре с указанным ID')
async def genres_delete(pk: int, db: Session = Depends(get_db)):
    """
    Удалить запись о жанре с указанным ID:
    """
    GenreService(db).delete(pk)
    # return None
