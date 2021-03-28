

import app

from constants import Constant
from utils.data_manager import DataManager
def run(api):
    """ function Which start the API
    args:
        api (flask_restful.Api): builded API
    Returns:
        None
    """

    api.run()

data_manager = DataManager()
if __name__ == "__main__":
    api , data = app.create_app()
    api.run(host=Constant.HOST, port=4000, debug=True)
    data_manager = data
