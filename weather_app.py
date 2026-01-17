"""
Simple Weather App - Fetches weather information for a given city
"""

import requests
import sys
from datetime import datetime


def get_weather(city_name):
    """
    Fetch weather data from OpenWeatherMap API for a given city.
    
    Args:
        city_name (str): The name of the city to get weather for
        
    Returns:
        dict: Weather data including temperature, description, humidity, etc.
        None: If the request fails
    """
    # API endpoint and key
    api_key = "d6294409cecab1718a4f0b156dc15e28"  # Free API key (limited requests)
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    # Parameters for the API request
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  # Use Celsius
    }
    
    try:
        # Make the API request
        response = requests.get(base_url, params=params, timeout=5)
        response.raise_for_status()  # Raise an error if the request fails
        
        # Return the JSON data
        return response.json()
    
    except requests.exceptions.RequestException as error:
        print(f"Error fetching weather data: {error}")
        return None


def display_weather(weather_data):
    """
    Display weather information in a nice, readable format.
    
    Args:
        weather_data (dict): Weather data from the API
    """
    if weather_data is None:
        print("Could not retrieve weather information.")
        return
    
    # Check if the city was found
    if weather_data.get("cod") != 200:
        print(f"City not found: {weather_data.get('message', 'Unknown error')}")
        return
    
    # Extract weather information
    city = weather_data.get("name")
    country = weather_data.get("sys", {}).get("country")
    temperature = weather_data.get("main", {}).get("temp")
    feels_like = weather_data.get("main", {}).get("feels_like")
    humidity = weather_data.get("main", {}).get("humidity")
    pressure = weather_data.get("main", {}).get("pressure")
    description = weather_data.get("weather", [{}])[0].get("description", "N/A")
    wind_speed = weather_data.get("wind", {}).get("speed")
    
    # Display the weather information
    print("\n" + "=" * 50)
    print(f"Weather for {city}, {country}")
    print("=" * 50)
    print(f"Temperature: {temperature}°C")
    print(f"Feels Like: {feels_like}°C")
    print(f"Description: {description.capitalize()}")
    print(f"Humidity: {humidity}%")
    print(f"Pressure: {pressure} hPa")
    print(f"Wind Speed: {wind_speed} m/s")
    print(f"Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50 + "\n")


def main():
    """
    Main function to run the weather app.
    """
    print("Welcome to the Simple Weather App!")
    print("-" * 50)
    
    # Get city name from user input or command line argument
    if len(sys.argv) > 1:
        city = " ".join(sys.argv[1:])
    else:
        city = input("Enter a city name: ").strip()
    
    if not city:
        print("City name cannot be empty!")
        return
    
    print(f"Fetching weather information for {city}...")
    
    # Get and display weather
    weather_data = get_weather(city)
    display_weather(weather_data)


if __name__ == "__main__":
    main()
