import sys
import os
from weather_data.data_reader import DataReader
from weather_data.data_calculator import DataCalculator

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
        print(f'Invalid file type!')
        exit(1)
    weather_data = None
    reader = DataReader(file_type,file_path)
    weather_data = reader()
    calculator = DataCalculator(weather_data, output_file)
    calculator()




if __name__ == "__main__":
    main()
