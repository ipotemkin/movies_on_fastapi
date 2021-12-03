from fastapi import APIRouter, status, Response
from app.implemented import director_service
from app.dao.model.directors import DirectorBM, DirectorUpdateBM

router = APIRouter(prefix='/directors', tags=['directors'])


@router.get('', summary='Получить всех режиссеров')
async def directors_get_all():
    """
    Получить всех режиссеров
    """
    return director_service.get_all()


@router.get('/{pk}', summary='Получить режиссера по его ID')
async def directors_get_one(pk: int):
    """
    Получить режиссера по ID:

    - **pk**: ID режиссера
    """
    return director_service.get_one(pk)


@router.post('', status_code=status.HTTP_201_CREATED, summary='Добавить режиссера',
             response_description="The created item")
async def directors_post(director: DirectorBM, response: Response):
    """
    Добавить режиссера:

    - **id**: ID режиссера - целое число (необязательный параметр)
    - **name**: имя режиссера (обязательный параметр)
    """
    new_obj = director_service.create(director.dict())
    response.headers['Location'] = f'{router.prefix}/{new_obj.id}'
    return []


@router.patch('/{pk}',
              # status_code=status.HTTP_204_NO_CONTENT,
              summary='Изменить запись режиссера с указанным ID')
async def directors_update(director: DirectorUpdateBM, pk: int):
    """
    Изменить запись режиссера с указанным ID:

    - **name**: изменить имя режиссера
    """
    return director_service.update(director.dict(), pk)


@router.delete('/{pk}', status_code=status.HTTP_200_OK, summary='Удалить запись режиссера с указанным ID')
async def directors_delete(pk: int):
    """
    Удалить запись режиссера с указанным ID:
    """
    director_service.delete(pk)
    # return None
