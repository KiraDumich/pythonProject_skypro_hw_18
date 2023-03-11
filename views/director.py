from flask_restx import Resource, Namespace

from dao.model.directors import DirectorSchema
from implemented import director_service

director_ns = Namespace('director')


@director_ns.route('/')
class DirectorsViews(Resource):
    def get(self):
        directors = director_service.get_all()
        result = DirectorSchema(many=True).dump(directors)
        return result, 200


@director_ns.route('/<int:uid>')
class DirectorsViews(Resource):
    def get(self, uid):
        directors = director_service.get_one(uid)
        result = DirectorSchema().dump(directors)
        return result, 200