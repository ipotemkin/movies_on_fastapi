# файл для создания DAO и сервисов чтобы импортировать их везде

# book_dao = BookDAO(db.session)
# book_service = BookService(dao=book_dao)
#
# review_dao = ReviewDAO(db.session)
# review_service = ReviewService(dao=review_dao)
from dao.model.directors import Director, DirectorBM
from dao.directors import DirectorDAO
from service.directors import DirectorService
from setup_db import db

director_dao = DirectorDAO(session=db.session, model=Director, schema=DirectorBM)
director_service = DirectorService(director_dao=director_dao)
