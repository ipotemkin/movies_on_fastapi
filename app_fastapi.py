import time

from fastapi import FastAPI, Request, status, Header, Response

from fastapi.responses import RedirectResponse, JSONResponse, PlainTextResponse
from uvicorn import run
# from implemented import director_service, directors_model, director_ns, auth_parser
# from setup_db import db
from flask import Flask
from sql_test import run_asql, run_sql_alchemy, get_one
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, Session
from errors import NotFoundError
from app.views import directors, genres, movies
from databases import Database


tags_metadata = [
    {
        'name': 'directors',
        'description': 'Операции с режиссерами',
    },
    {
        'name': 'genres',
        'description': 'Операции с жанрами',
    },
    {
        'name': 'movies',
        'description': 'Операции с фильмами',
    },
]


app_fastapi = FastAPI(title='Movies API on FastAPI',
                      description='This is a refactored app from lessons 18 and 19',
                      version='1.0.0',
                      openapi_tags=tags_metadata)

app_fastapi.include_router(movies.router)
app_fastapi.include_router(directors.router)
app_fastapi.include_router(genres.router)


@app_fastapi.exception_handler(404)
@app_fastapi.exception_handler(NotFoundError)
def not_found_error(request: Request, exc: NotFoundError):
    return JSONResponse(
        status_code=404,
        content={'message': "Not Found"}
    )


# перенаправляем на страницу документации
@app_fastapi.get('/')
async def index():
    return RedirectResponse(url='/docs')


@app_fastapi.get('/aio/directors')
async def aio_directors_get_all():
    """
    Получить всех режиссеров
    """
    dbase = Database("sqlite:///movies.db")
    t0 = time.perf_counter()
    # res = await run_asql('select * from director')
    res = await dbase.fetch_all(query='select * from director')
    elapsed = time.perf_counter() - t0
    print('aio with databases [%0.8fs]' % elapsed)
    return res


@app_fastapi.get('/aio/directors/{pk}')
async def aio_directors_get_one(pk: int):
    """
    Получить режиссера по ID
    """
    return await get_one(f'select * from director where id = {pk} limit 1')


if __name__ == '__main__':
    run(
        "app_fastapi:app_fastapi",
        host='localhost',
        port=8000,
        reload=True
    )
