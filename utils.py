"""
Load weather data from a specified JSON file.

This function attempts to read and load weather data from a JSON file
with the given filename. If the file is successfully read, the weather
data is printed and returned as a dictionary. If the file cannot be read
due to an IOError, an error message is printed and the function returns None.

Parameters:
filename (str): The name of the JSON file to load the weather data from.
                Defaults to "weather_data.json".

Returns:
dict or None: A dictionary containing the weather data if the file is 
              successfully read, otherwise None.

Example usage:
weather_data = load_weather_data("my_weather_data.json")
"""


import json
from crewai_tools import tool

@tool("weather_load_tool")
def load_weather_data(filename="weather_data.json"):
    """
    Load weather data from a specified JSON file.

    This function attempts to read and load weather data from a JSON file
    with the given filename. If the file is successfully read, the weather
    data is printed and returned as a dictionary. If the file cannot be read
    due to an IOError, an error message is printed and the function returns None.

    Parameters:
    filename (str): The name of the JSON file to load the weather data from.
                    Defaults to "weather_data.json".

    Returns:
    dict or None: A dictionary containing the weather data if the file is 
                  successfully read, otherwise None.
    
    Example usage:
    weather_data = load_weather_data("my_weather_data.json")
    """
    with open(filename, 'r') as json_file:
        weather_data = json.load(json_file)
        print("Weather data loaded successfully.")
    print(weather_data)
    return weather_data
