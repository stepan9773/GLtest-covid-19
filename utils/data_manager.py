import os
from datetime import datetime

import numpy as np
import pandas as pd
import requests

from constants import Constant


class DataManager:

    def __init__(self):
        self.timer = datetime.now().day

    def get_info(self):
        if datetime.now().day is self.timer:
            info = pd.read_csv('cash/owid-covid-data.csv')
            return info
        else:
            self.timer = datetime.now().day
            DataManager.download_csv()
            info = pd.read_csv('cash/owid-covid-data.csv')
            return info

    @staticmethod
    def get_last_info_by_country(country):
        data = DataManager.get_info(data_manager)
        last_data_per_day = data[data['location'] == country][-1:].replace(np.nan, 0)
        return last_data_per_day.to_dict()

    @staticmethod
    def download_csv():
        req = requests.get(Constant.DATA_URL)
        url_content = req.content
        try:
            os.remove('cash/owid-covid-data.csv')
        except:
            pass
        csv_file = open('cash/owid-covid-data.csv', 'wb')
        csv_file.write(url_content)
        csv_file.close()


data_manager = DataManager()
