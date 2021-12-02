from fastapi import FastAPI
from uvicorn import run
from implemented import director_service, directors_model, director_ns, auth_parser
from setup_db import db
from flask import Flask
from sql_test import run_asql, run_sql_alchemy

app_fastapi = FastAPI(title='Movies API on FastAPI',
                      description='This is a refactored app from lessons 18 and 19',
                      version='1.0.0')

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# # db.init_app(dict(SQLALCHEMY_DATABASE_URI='sqlite:///movies.db', SQLALCHEMY_TRACK_MODIFICATIONS=False))
# db.init_app(app)


# @app_fastapi.get('/')
@app_fastapi.get('/directors')
async def get_all_directors():
    """
    Получить всех режиссеров
    """
    return await run_asql('select * from director')


@app_fastapi.get('/directors/{pk}')
async def get_one_director(pk: int):
    """
    Получить режиссера по ID
    """
    return await run_asql(f'select * from director where id = {pk} limit 1')


@app_fastapi.get('/genres')
async def get_all_genres():
    """
    Получить все жанры
    """
    return await run_asql('select * from genre')


@app_fastapi.get('/genres/{pk}')
async def get_one_genre(pk: int):
    """
    Получить жанр по ID
    """
    return await run_asql(f'select * from genre where id = {pk} limit 1')


@app_fastapi.get('/movies', description='Получить все фильмы')
async def get_all_movies():
    """
    Получить все фильмы
    """
    return await run_asql('select * from movie')


@app_fastapi.get('/movies/{pk}')
async def get_one_movie(pk: int):
    """
    Получить фильм по ID
    """
    return await run_asql(f'select * from movie where id = {pk} limit 1')


if __name__ == '__main__':
    run(
        "app_fastapi:app_fastapi",
        host='localhost',
        port=8000,
        reload=True
    )
