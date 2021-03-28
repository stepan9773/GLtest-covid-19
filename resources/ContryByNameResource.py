from flask import jsonify
from flask_restful import Resource

from utils.data_manager import DataManager


class CountryByNameResource(Resource):
    def get(self, country):
        data = DataManager.get_last_info_by_country(country)
        result = jsonify({"data": data})
        return result
