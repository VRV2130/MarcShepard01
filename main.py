import requests
from tabulate import tabulate

api_key = 'e0fd96f267a7c01a2e089a841f1fd1c8' 
#Stupid. You shouldn't put your API key on public docuements! Poeple can steal it!.
def get_weather(country, city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        main_weather = data['weather'][0]['main']
        description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        print(f"Weather in {city}, {country}:")
        print("----------------------------")
        weather_data = [
            ['Main', main_weather],
            ['Description', description],
            ['Temperature', f"{temperature}°C"],
            ['Humidity', f"{humidity}%"],
            ['Wind Speed', f"{wind_speed} m/s"]
        ]
        print(tabulate(weather_data, headers=['Attribute', 'Value'], tablefmt='grid'))
    
    else:
        print("Failed to fetch weather data.")
        print(response.status_code)
        print(response.content)

while True:
    countryU = input("Enter the country: ")
    cityU = input("Enter the city: ")

    get_weather(countryU, cityU)

    choice = input("Do you want to check weather for another location? (y/n): ")
    if choice.lower() != 'y':
        break
