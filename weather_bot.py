import requests
from token_config import TOKEN_WEATHER


def get_weather():
    data_l = {'lat': 42.266541672193696, 'lon': 42.71802746570188, 'appid': TOKEN_WEATHER, 'units': 'metric'}
    url_weather = 'https://api.openweathermap.org/data/2.5/weather'
    resp_weather = requests.get(url_weather, data_l)
    value = resp_weather.json()
    li_value = [value['main']['temp'], value['weather'][0]['description'],
                value['wind']['speed'], value['main']['pressure'], value['name']]
    city = li_value[4]
    temp = li_value[0]
    sky = li_value[1]
    sky = sky.capitalize()
    wind = li_value[2]
    pressure = li_value[3]
    weather_result = (f'Weather in {city} now:\n'
                      f'Temperatures: {temp} °C\n'
                      f'Sky: {sky}\n'
                      f'Wind speed: {wind} m/s\n'
                      f'Pressure: {pressure} mm Hg')

    return weather_result
