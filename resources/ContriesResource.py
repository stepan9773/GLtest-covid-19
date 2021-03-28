from flask import jsonify
from flask_restful import Resource

from utils.data_manager import DataManager, data_manager


class CountriesResource(Resource):
    def get(self):
        covid_info = DataManager.get_info(data_manager)
        locations = covid_info.location.unique()
        result = jsonify({"location": list(locations)})
        return result
