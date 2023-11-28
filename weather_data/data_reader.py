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
        data_json = {}
        prption = []
        wthr = []
        tmpre = []
        with open(self.file_path,'r') as f:
            weather_list = f.readlines()
            if not isinstance(weather_list, list):
                print('Unexpected format, should be list')
                exit(1)
            for line in weather_list:
                if 'temperature' in line:
                    line = line.split()
                    tmpre.append(int(line[1][0:-1]))
                if 'precipitation' in line:
                    line = line.split()
                    prption.append(float(line[1][0:-1]))
                if 'weather' in line:
                    line = line.split()
                    wthr.append(line[1][0:-1])
        data_json['temperature'] = tmpre
        data_json['weather'] = wthr
        data_json['precipitation'] = prption
        return data_json
    def read_weather_data_csv(self):
        data_csv = {}
        prption = []
        wthr = []
        tmpre = []
        with open(self.file_path,'r') as f:
            weather_data_reader = csv.reader(f)
            first_row = True 
            for row in weather_data_reader:
                if first_row:
                    first_row = False
                    continue
                tmpre.append(int(row[0]))
                wthr.append(row[1])
                prption.append(float(row[2]))
        data_csv['weather'] = wthr
        data_csv['temperature'] = tmpre
        data_csv['precipitation'] = prption
        return data_csv

        