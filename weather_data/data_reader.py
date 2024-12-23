#import standard library modules and json/csv files
import json
import csv
import sys
import os
#define class to read the weather report based on file type
class DataReader:
    #initialize file path and type
    def __init__(self, file_type, file_path):
        self.file_type = file_type
        self.file_path = file_path
    #use __call__ function to direct to which file type to read
    def __call__(self):
        if self.file_type == 'json':
            return self.read_weather_data_json()
        elif self.file_type == 'csv':
            return self.read_weather_data_csv()
    # read the weather data from a json file and validate all keys are present
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
                            key_str += ', '
                    print(f'Some entries are missing required keys: {key_str}.')
                    exit(1)
                else:
                    data['weather'].append(entry['weather'])
                    data['temperature'].append(int(entry['temperature']))
                    data['precipitation'].append(float(entry['precipitation']))
        f.close()
        return data
    # read weather data from csv file and validate all keys are present
    def read_weather_data_csv(self):
        data = {'temperature': [], 'weather': [], 'precipitation': []}
        expected_keys = ['temperature', 'weather', 'precipitation']
        with open(self.file_path,'r') as f:
            csv_data = csv.DictReader(f)
            missing_keys = []
            for key in expected_keys:
                if key not in csv_data.fieldnames:
                    missing_keys.append(key)
            if missing_keys != []:
                key_str = ''
                for i in range(len(missing_keys)):
                    key_str += missing_keys[i]
                    if missing_keys[i] == missing_keys[-1]:
                        continue
                    else:
                        key_str += ', '
                print(f'Some entries are missing required keys: {key_str}.')
                exit(1)
                    
            for entry in csv_data:
                if entry['temperature'] == '':
                    print("Error in data format: could not convert string to float: ''. Check the numeric values in the file.")
                    exit(1)
                data['weather'].append(entry['weather'])
                data['temperature'].append(int(entry['temperature']))
                data['precipitation'].append(float(entry['precipitation']))
        f.close()
        return data

        