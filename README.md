# 🌤️ Simple Weather App

A beginner-friendly Python application that fetches and displays real-time weather information for any city in the world.

## What Does This Program Do?

This weather app is a simple Python program that:
- Takes a city name as input (from the user or command line)
- Connects to OpenWeatherMap API to fetch real-time weather data
- Displays weather information in a nice, readable format
- Shows temperature, humidity, wind speed, pressure, and weather description

## Features

✨ **Easy to Use** - Simply enter a city name and get instant weather information  
🌍 **Works Worldwide** - Get weather for any city around the globe  
📊 **Detailed Information** - Shows temperature, humidity, wind speed, and more  
⚡ **Fast & Lightweight** - Minimal dependencies and quick execution  
🎓 **Beginner-Friendly Code** - Well-commented and easy to understand  

## Prerequisites

Before running this program, you need:
- **Python 3.6 or higher** installed on your computer
- **pip** (Python package manager) - usually comes with Python

To check if you have Python installed, open your terminal/command prompt and type:
bash
python --version


## Installation

### Step 1: Clone or Download the Repository
bash
git clone https://github.com/YOUR-USERNAME/simple-weather-app.git
cd simple-weather-app


### Step 2: Create a Virtual Environment (Optional but Recommended)
A virtual environment keeps your project dependencies isolated.

**On Windows:**
bash
python -m venv venv
venv\Scripts\activate


**On macOS/Linux:**
bash
python3 -m venv venv
source venv/bin/activate


### Step 3: Install Dependencies
Install the required packages listed in `requirements.txt`:
bash
pip install -r requirements.txt


This will install the `requests` library needed for making API calls.

## Usage

### Method 1: Interactive Mode
Run the program and it will ask you to enter a city name:
bash
python weather_app.py


Then type a city name when prompted:

Enter a city name: London


### Method 2: Command Line Argument
Pass the city name directly as an argument:
bash
python weather_app.py New York


## Example Output
=============================================
Weather for London, GB
=============================================
Temperature: 15°C
Feels Like: 14°C
Description: Partly cloudy
Humidity: 65%
Pressure: 1013 hPa
Wind Speed: 3.5 m/s
Last Updated: 2024-01-17 14:30:45
============================================


## Project Structure
simple-weather-app/
│
├── weather_app.py          # Main Python program
├── requirements.txt        # List of dependencies
├── README.md              # This file - documentation
├── .gitignore            # Files to ignore in git
└── LICENSE               # License information


## How It Works

### 1. **User Input**
The program asks for a city name or accepts it as a command-line argument.

### 2. **API Request**
It sends a request to OpenWeatherMap's free weather API with the city name.

### 3. **Data Processing**
The program receives JSON data with weather information and extracts the relevant details.

### 4. **Display Results**
Weather information is formatted nicely and displayed to the user.

## Understanding the Code

### Main Functions

**`get_weather(city_name)`**
- Connects to the OpenWeatherMap API
- Sends a request with the city name
- Returns weather data as a dictionary
- Handles errors gracefully

**`display_weather(weather_data)`**
- Takes the weather data returned from the API
- Extracts specific information (temperature, humidity, etc.)
- Formats and prints the data in a readable way

**`main()`**
- The entry point of the program
- Gets input from the user
- Calls the other functions in the right order

## Troubleshooting

### "ModuleNotFoundError: No module named 'requests'"
**Solution:** You didn't install the dependencies. Run:
bash
pip install -r requirements.txt


### "City not found"
**Solution:** Make sure you spelled the city name correctly. Try using the English name of the city.

### "Connection error" or "Timeout error"
**Solution:** Check your internet connection and try again.

### API Limit Reached
The free API key has a limit of 60 requests per minute. If you hit the limit, wait a minute before trying again.

## API Information
This project uses the **OpenWeatherMap Free API**:
- Website: https://openweathermap.org/api
- Free Tier: 60 calls per minute, 1,000,000 calls per month
- No credit card required to sign up

## What You Can Learn From This Project
1. **Making API Requests** - How to use the `requests` library
2. **Error Handling** - Using try-except blocks safely
3. **Data Processing** - Working with JSON data
4. **Functions** - Creating reusable, well-documented functions
5. **Command Line Arguments** - Using `sys.argv`
6. **User Input** - Getting input from users
7. **Code Documentation** - Writing docstrings and comments

## Next Steps / Enhancements
Once you're comfortable with this project, try adding:
- ✅ Save weather to a file
- ✅ Get weather for multiple cities at once
- ✅ Show weather forecast for upcoming days
- ✅ Add a GUI using tkinter
- ✅ Store city data in a database
- ✅ Add unit conversion (Fahrenheit/Celsius)

## Troubleshooting Common Issues
| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError: requests` | Run `pip install -r requirements.txt` |
| `City not found` | Check spelling and use English city names |
| `Connection timeout` | Check your internet connection |
| No output | Make sure you entered a valid city name |

## License
This project is open source and available under the MIT License. See the LICENSE file for details.

## Contributing
Feel free to fork this project and submit pull requests with improvements!

## Support
If you encounter any issues:
1. Check the Troubleshooting section
2. Read the comments in the code
3. Open an issue on GitHub with details about the problem
