import requests

api_key = 'Yf1150dcc35f77a426b1b58d28732718aCa'  # Replace with your OpenWeatherMap API key

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
        print(f"Main: {main_weather}")
        print(f"Description: {description}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("Failed to fetch weather data.")

country = input("Enter the country: ")
city = input("Enter the city: ")

get_weather(country, city)