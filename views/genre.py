from flask_restx import Resource, Namespace

from dao.model.genres import GenreSchema
from implemented import genre_service

genre_ns = Namespace('genre')


@genre_ns.route('/')
class GenreViews(Resource):
    def get(self):
        genre_object = genre_service.get_all()
        result = GenreSchema(many=True).dump(genre_object)
        return result, 200


@genre_ns.route('/<int:uid>')
class GenreViews(Resource):
    def get(self, uid):
        genres_object = genre_service.get_one(uid)
        result = GenreSchema().dump(genres_object)
        return result, 200