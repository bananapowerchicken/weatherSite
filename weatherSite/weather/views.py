from django.shortcuts import render
import requests
from .models import City

def index(request):
    appid = '5f2887a8ea1643c8f436a30eeeec5f6e'
    # units=metric чтобы данные в цельсии
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    # city = 'Moscow'
    cities = City.objects.all()
    all_cities = []

    for city in cities:
        res = requests.get(url.format(city)).json()

        # словарь с нужными мне данными из запроса, можно расширять
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],  # извлекаем данные из json запроса
            'icon:': res["weather"][0]["icon"]
        }

        all_cities.append(city_info)

    # передаем эти данные в шаблон index.html
    context = {
        'all_info': all_cities
    }

    return render(request, 'weather/index.html', context)  # по умолчанию все шаблоны
# ищутся в папке templates

