from flask import request, Blueprint
from flask_restful import Api, Resource

from .models import sarampion_panama
from .schema import VacunasSchema

vacunas_v1_0_bp = Blueprint('vacunas_v1_0_bp', __name__)

vacuna_schema = VacunasSchema()

api = Api(vacunas_v1_0_bp)

class Listar(Resource):
    def get_all(self):
        response = sarampion_panama.get_all()
        result = vacuna_schema.dump(response, many=True)
        return result


api.add_resource(Listar, '/api/v1.0/vacunas/', endpoint='vacunas_list_resource')
