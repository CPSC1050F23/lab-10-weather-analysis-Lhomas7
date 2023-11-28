class DataCalculator:
    
    def __init__(self, weather_data, file_path):
        self.weather_data = weather_data
        self.file_path = file_path

    def __call__(self):
        if self.weather_data is None or 'temperatures' not in self.weather_data or 'weather' not in self.weather_data or 'precipitations' not in self.weather_data:
            print("Invalid weather data.")
            exit(1)
        
        average_temp = self.calculate_average_temperature()
        max_temp = self.calculate_maximum_temperature()
        min_temp = self.calculate_minimum_temperature()
        average_precipitation = self.calculate_average_precipitation()
        weather_summary = self.summarize_weather_conditions()
        self.display_results(average_temp, max_temp, min_temp, average_precipitation, weather_summary)

    def calculate_average_temperature(self):
        sum_temp = 0
        for temp in self.weather_data['temperature']:
            sum_temp += temp
        avg_temp = sum_temp / len(self.weather_data['temperature'])
        return avg_temp

    def calculate_maximum_temperature(self):
        max_temp = 0
        for temp in self.weather_data['temperature']:
            if temp > max_temp:
                max_temp = temp
        return max_temp

    def calculate_minimum_temperature(self):
        min_temp = self.weather_data['temperature'][0]
        for temp in self.weather_data['temperature']:
            if temp < min_temp:
                min_temp = temp
        return min_temp

    def calculate_average_precipitation(self):
        sum_prec = 0
        for precip in self.weather_data['precipitation']:
            sum_prec += precip
        avg_precip = sum_prec / len(self.weather_data['precipitation'])
        return avg_precip

    def summarize_weather_conditions(self):
        weather_summary = {}
        count = 0
        for condition in self.weather_data['weather']:
            if condition == 'snowy':
                count += 1
            weather_summary['snowy'] = count
        count = 0
        for condition in self.weather_data['weather']:
            if condition == 'sunny':
                count += 1
            weather_summary['sunny'] = count
        count = 0
        for condition in self.weather_data['weather']:
            if condition == 'rainy':
                count += 1
            weather_summary['rainy'] = count
        count = 0
        for condition in self.weather_data['weather']:
            if condition == 'partly cloudy':
                count += 1
            weather_summary['partly cloudy'] = count
        count = 0
        for condition in self.weather_data['weather']:
            if condition == 'overcast':
                count += 1
            weather_summary['overcast'] = count
        return weather_summary

    def display_results(self, average_temp, max_temp, min_temp, average_precipitation, weather_summary):
        with open(self.file_path,'w') as f:
            f.write(f"Average Temperature: {average_temp}")
            f.write(f"Maximum Temperature: {max_temp}")
            f.write(f"Minimum Temperature: {min_temp}")
            f.write(f"Average Precipitation: {average_precipitation}")
            f.write(f"Weather Summary: {weather_summary}")


