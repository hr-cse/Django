from django.shortcuts import render
import requests
url = 'https://samples.openweathermap.org/data/2.5/weather?q={},uk&appid=b6907d289e10d714a6e88b30761fae22'
r = requests.get(url.format("Dhaka")).json()


def index(request):
    return render(request, 'weather/weather.html')