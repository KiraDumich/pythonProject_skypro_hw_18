# Здесь бизнес логика, в виде классов или методов. Сюда импортируются DAO классы из пакета dao и модели из dao.model
# некоторые методы могут оказаться просто прослойкой между dao и views,
# но чаще всего будет какая-то логика обработки данных сейчас или в будущем.
from dao.movies import MovieDAO
from dao.directors import DirectorDAO
from dao.genres import GenreDAO


# сервисы для фильма
class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_all(self, filters):
        if filters.get('director_id') is not None:
            movies = self.dao.get_by_director_id(filters.get('director_id'))
        elif filters.get('genre_id') is not None:
            movies = self.dao.get_by_genre_id(filters.get('genre_id'))
        elif filters.get('year') is not None:
            movies = self.dao.get_by_year(filters.get('year'))
        else:
            movies = self.dao.get_all()

        return movies

    def create(self, movie_a):
        return self.dao.create(movie_a)

    def update(self, movie_a):
        self.dao.update(movie_a)
        return self.dao

    def delete(self, uid):
        self.dao.delete(uid)


# сервисы для режиссёров
class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, director_a):
        return self.dao.create(director_a)

    def update(self, director_a):
        self.dao.update(director_a)
        return self.dao

    def delete(self, uid):
        self.dao.delete(uid)


# сервисы для жанров
class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, genre_a):
        return self.dao.create(genre_a)

    def update(self, genre_a):
        self.dao.update(genre_a)
        return self.dao

    def delete(self, uid):
        self.dao.delete(uid)