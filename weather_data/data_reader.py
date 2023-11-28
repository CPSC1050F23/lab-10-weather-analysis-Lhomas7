import json
import csv
import sys
import os

class DataReader:
    
    def __init__(self, file_type, file_path):
        self.file_type = file_type
        self.file_path = file_path

    def __call__(self):
        if self.file_type == 'json':
            return self.read_weather_data_json()
        elif self.file_type == 'csv':
            return self.read_weather_data_csv()

    def read_weather_data_json(self):
        data = {'temperature': [], 'weather': [], 'precipitation': []}
        expected_keys = ['temperature', 'weather', 'precipitation']
        with open(self.file_path,'r') as f:
            json_data = json.load(f)
            if not isinstance(json_data, list):
                print("Error in data format: could not convert string to float: ''. Check the numeric values in the file.")
                exit(1)
            for entry in json_data:
                missing_keys = []
                for key in expected_keys:
                    if key not in entry:
                        missing_keys.append(key)
                if missing_keys:
                    key_str = ''
                    for i in range(len(missing_keys)):
                        key_str += missing_keys[i]
                        if missing_keys[i] == missing_keys[-1]:
                            continue
                        else:
                            key_str += ','
                    print(f'Some entries are missing required keys: {key_str}')
                    exit(1)
                else:
                    data['weather'].append(entry['weather'])
                    data['temperature'].append(entry['temperature'])
                    data['precipitation'].append(entry['precipitation'])
        f.close()
        return data

    def read_weather_data_csv(self):
        data = {'temperature': [], 'weather': [], 'precipitation': []}
        expected_keys = ['temperature', 'weather', 'precipitation']
        with open(self.file_path,'r') as f:
            csv_data = csv.DictReader(f)

            if not isinstance(csv_data, list):
                print("Error in data format: could not convert string to float: ''. Check the numeric values in the file.")
                exit(1)
            for entry in csv_data.fieldnames:
                missing_keys = []
                for key in expected_keys:
                    if key not in entry:
                        missing_keys.append(key)
                if missing_keys:
                    key_str = ''
                    for i in range(len(missing_keys)):
                        key_str += missing_keys[i]
                        if missing_keys[i] == missing_keys[-1]:
                            continue
                        else:
                            key_str += ','
                    print(f'Some entries are missing required keys: {key_str}')
                    exit(1)
            for entry in csv_data:
                data['weather'].append(entry['weather'])
                data['temperature'].append(entry['temperature'])
                data['precipitation'].append(entry['precipitation'])
        f.close()
        return data

        