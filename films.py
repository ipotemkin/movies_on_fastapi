# основной файл приложения. здесь конфигурируется фласк, сервисы, SQLAlchemy и все остальное что требуется
# для приложения. этот файл часто является точкой входа в приложение

from __init__ import app

from setup_db import db
from dao.model.movies import Movie
from dao.model.directors import Director
from dao.model.genres import Genre


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Movie': Movie, 'Director': Director, 'Genre': Genre}


if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)
