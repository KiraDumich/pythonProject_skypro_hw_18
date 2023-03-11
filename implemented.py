# файл для создания DAO и сервисов, чтобы импортировать их везде
from dao.movies import MovieDAO
from dao.genres import GenreDAO
from dao.directors import DirectorDAO

from service.entity_name import DirectorService
from service.entity_name import GenreService
from service.entity_name import MovieService

from setup_db import db

# контейнеры для данных
director_dao = DirectorDAO(session=db.session)
genre_dao = GenreDAO(session=db.session)
movie_dao = MovieDAO(session=db.session)

director_service = DirectorService(dao=director_dao)
genre_service = GenreService(dao=genre_dao)
movie_service = MovieService(dao=movie_dao)