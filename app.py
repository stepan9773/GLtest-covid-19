from flask import Flask, render_template
from flask_cors import CORS
from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint

from utils.data_manager import DataManager

APP_NAME = "covid"
APP_PREFIX = ""


def create_app():
    """
    fuction build app

    args:
        config (flask.Config): config: API start configuration
    Returns:
         app (Flask): application
    """

    app = Flask(APP_NAME)
    api = Api(app, prefix=APP_PREFIX)
    register_resource(api)
    CORS(app)

    SWAGGER_URL = f'/swagger'
    API_URL = '/static/swagger.yaml'
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL
        , API_URL
        , config={
            'app_name': 'Lab7 API Documentation'
        }
    )

    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
    data_manager = DataManager()

    @app.route('/')
    def home():
        return render_template('index.html')

    return app, data_manager


def register_resource(api):
    """
    Connect to API rotes resources
    args:
        api: API which connect the resources routes
    Returns:
         None
    """
    from resources.ContriesResource import CountriesResource
    from resources.ContryByNameResource import CountryByNameResource
    # from resources.indexResource import indexResource

    api.add_resource(CountriesResource, '/location')
    api.add_resource(CountryByNameResource, '/location/<string:country>')
    # api.add_resource(indexResource, '/')
