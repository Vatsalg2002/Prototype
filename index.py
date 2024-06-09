"""
This script fetches the current weather data and air quality index (AQI) for the user's location based on their IP address, and saves the data to a JSON file.

Key functionalities include:
1. Retrieving the user's geographical location (latitude and longitude) using their IP address via the ipinfo.io API.
2. Fetching the current weather data and AQI using the WeatherAPI.
3. Saving the fetched weather data to a JSON file for further use.

Functions:
- get_location_by_ip: Uses the ipinfo.io API to get the user's geographical coordinates.
- get_weather_data: Fetches weather and AQI data from the WeatherAPI using the coordinates obtained.
- save_weather_data: Saves the fetched weather data to a specified JSON file.
- main: Orchestrates the sequence of steps: retrieving location, fetching weather data, and saving the data.

Usage:
Run the script directly to retrieve and save the current weather data based on the user's IP location.
Ensure that you have an internet connection and the required API key for WeatherAPI.

Requirements:
- requests: To handle HTTP requests.
- json: To handle JSON data.

Example:
    python script_name.py

Make sure to replace the placeholder API key with a valid key from WeatherAPI.
"""


import requests
import json

def get_location_by_ip():
    try:
        response = requests.get("https://ipinfo.io")
        response.raise_for_status()
        data = response.json()
        loc = data['loc'].split(',')
        latitude = loc[0]
        longitude = loc[1]
        return latitude, longitude
    except requests.RequestException as e:
        print(f"Error fetching location: {e}")
        return None, None

def get_weather_data(latitude, longitude):
    api_key = "3034d932dd834254b27180909240806"
    api_url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={latitude},{longitude}&aqi=yes"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def save_weather_data(weather_data, filename="weather_data.json"):
    try:
        with open(filename, 'w') as json_file:
            json.dump(weather_data, json_file)
        print(f"Weather data saved to {filename}")
    except IOError as e:
        print(f"Error saving weather data to file: {e}")

def main():
    # Step 1: Get user's location
    latitude, longitude = get_location_by_ip()
    
    if latitude and longitude:
        print(f"Location: Latitude = {latitude}, Longitude = {longitude}")
        
        # Step 2: Get weather data
        weather_data = get_weather_data(latitude, longitude)
        
        if weather_data:
            print("Weather data retrieved successfully.")
            save_weather_data(weather_data)
        else:
            print("Failed to retrieve weather data.")
    else:
        print("Failed to retrieve location data.")

if __name__ == "__main__":
    main()
