import json
import csv

class DataReader:
    
    def __init__(self, file_type, file_path):
        pass

    def __call__(self):
        if self.file_type == 'json':
            return self.read_weather_data_json()
        elif self.file_type == 'csv':
            return self.read_weather_data_csv()

    def read_weather_data_json(self):
        pass

    def read_weather_data_csv(self):
        pass