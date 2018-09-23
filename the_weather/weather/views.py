from django.shortcuts import render
import requests
from .models import City



def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=0cf53fc17073afb3f22fd263aea3a466'
    cities = City.objects.all()
    weather_data = []
    for city in cities:

        r = requests.get(url.format(city)).json()
        city_weather = {
            'city' : city,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }
        weather_data.append(city_weather)
    context = {
        'weather_data' : weather_data
    }

    return render(request, 'weather/weather.html', context)