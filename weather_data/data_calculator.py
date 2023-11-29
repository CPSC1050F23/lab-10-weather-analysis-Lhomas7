# create calculator class to calculate data to be displayed in weather summary
class DataCalculator:
    # initialize weather data from data reader class and the file path
    def __init__(self, weather_data, file_path):
        self.weather_data = weather_data
        self.file_path = file_path
    #define __call__ function to get quick acccess to attributes made by each clas function and display the results
    def __call__(self):
        
        average_temp = self.calculate_average_temperature()
        max_temp = self.calculate_maximum_temperature()
        min_temp = self.calculate_minimum_temperature()
        average_precipitation = self.calculate_average_precipitation()
        weather_summary = self.summarize_weather_conditions()
        self.display_results(average_temp, max_temp, min_temp, average_precipitation, weather_summary)
    # calculate the average temperature
    def calculate_average_temperature(self):
        avg_temp = sum(self.weather_data['temperature']) / len(self.weather_data['temperature'])
        avg_temp2 = avg_temp // 1
        if avg_temp - avg_temp2 >= 0.5:
            avg_temp2 += 1
        return round(avg_temp2)
        
    #calculate the maximum temperature
    def calculate_maximum_temperature(self):
        max_temp = 0
        for temp in self.weather_data['temperature']:
            if temp > max_temp:
                max_temp = temp
        return round(max_temp)

    def calculate_minimum_temperature(self):
        min_temp = self.weather_data['temperature'][0]
        for temp in self.weather_data['temperature']:
            if temp < min_temp:
                min_temp = temp
        return round(min_temp)
    #calculate the minimum temperature
    def calculate_average_precipitation(self):
        sum_prec = 0
        for precip in self.weather_data['precipitation']:
            sum_prec += precip
        avg_precip = sum_prec / len(self.weather_data['precipitation'])
        return round(avg_precip, 2)
    #summarize the weather data
    def summarize_weather_conditions(self):
        weather_summary = {}
        for condition in self.weather_data['weather']:
                if condition in weather_summary:
                    weather_summary[condition] += 1
                else:
                    weather_summary[condition] = 1

        return weather_summary
    #display the results by writing the data to an output file given to the file_path
    def display_results(self, average_temp, max_temp, min_temp, average_precipitation, weather_summary):
        with open(self.file_path,'w') as f:
            f.write(f"Average Temperature: {average_temp:.0f}\n")
            f.write(f"Maximum Temperature: {max_temp}\n")
            f.write(f"Minimum Temperature: {min_temp}\n")
            f.write(f"Average Precipitation: {average_precipitation:.2f}\n")
            f.write(f"Weather Summary: {weather_summary}\n")
        f.close()


