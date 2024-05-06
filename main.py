import argparse

import pyfiglet
import requests
from decouple import config
from simple_chalk import chalk

API_KEY = config('API_KEY')
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

WEATHER_ICON = {
    "01d": "🌞",
    "02d": "⛅",
    "03d": "☁",
    "04d": "☁",
    "09d": "🌧",
    "10d": "🌧",
    "11d": "⛈",
    "13d": "🌨",
    "50d": "🌪",
    "01n": "🌙",
    "02n": "☁",
    "03n": "☁",
    "04n": "☁",
    "09n": "🌧",
    "10n": "🌧",
    "11n": "⛈",
    "13n": "🌨",
    "50n": "🌪",
}

parser = argparse.ArgumentParser(description='check the weather for certain city/country')
parser.add_argument('country', help='city/country to check')
args = parser.parse_args()
url = f"{BASE_URL}/?q={args.country}&appid={API_KEY}&units=metric"

response = requests.get(url)
if response.status_code != 200:
    print(chalk.red('Error: Unable to retrieve weather information'))
    exit()

data = response.json()
temp = data['main']['temp']
temp_min = data['main']['temp_min']
temp_max = data['main']['temp_max']
feels_like = data['main']['feels_like']
description = data['weather'][0]['description']
icon = data['weather'][0]['icon']
city = data['name']
country = data['sys']['country']

weather_icon = WEATHER_ICON.get(icon, '')
output = f"{pyfiglet.figlet_format(city)}, {country}\n\n"
output += f"{weather_icon} {description}\n"
output += f"Temperature: {temp}°C\n"
output += f"feels like: {feels_like}°C\n"
output += f"temp_min: {temp_min}, temp_max: {temp_max}"

print(chalk.green(output))
