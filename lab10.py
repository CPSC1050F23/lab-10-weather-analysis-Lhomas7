"""
Author:         Landon Thomas
Date:           11/7/23
Assignment:     Lab 08
Course:         CPSC1051
Lab Section:    004

CODE DESCRIPTION:
This program models an analysis of a weather report, taking into account
weather conditions, temperature, and precipitation. It uses 2 classes, DataReader and DataCalculator in separate modules
to execute the program. The input is a file that must be either Json or Csv and the code validates that. 
The ouput is to a txt file that displays the average temperature, max and minimum temperature, average precipitation, and weather summary.
"""
#import modules including the created class modules
import sys
import os
from weather_data.data_reader import DataReader
from weather_data.data_calculator import DataCalculator
#create main class that validates if all command arguments are present, if the file exists, and if the file type is json or csv or neither then displays the data to a new output file
def main():
    if len(sys.argv) != 3:
        print('Need lab10.py, input_file, and output_file in command line')
        exit(1)
    print(f"Using file {sys.argv[1]}")
    if not os.path.exists(sys.argv[1]):
        print('File does not exist')
        exit(1)
    file_path = sys.argv[1]
    file_type = file_path.split(".")[-1]
    output_file = sys.argv[2]

    if file_type not in ['csv', 'json']:
        print(f'Invalid file type {file_type} detected! File type must be csv or json.')
        exit(1)
    weather_data = None
    reader = DataReader(file_type,file_path)
    weather_data = reader()
    calculator = DataCalculator(weather_data, output_file)
    calculator()



#run the main code
if __name__ == "__main__":
    main()
