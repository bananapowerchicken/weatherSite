from django.shortcuts import render
import requests

def index(request):
    appid = '5f2887a8ea1643c8f436a30eeeec5f6e'
    # units=metric чтобы данные в цельсии
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    city = 'Moscow'
    res = requests.get(url.format(city)).json()

    # словарь с нужными мне данными из запроса, можно расширять
    city_info = {
        'city': city,
        'temp': res["main"]["temp"],  # извлекаем данные из json запроса
        'icon:': res["weather"][0]["icon"]
    }

    # передаем эти данные в шаблон index.html
    context = {
        'info': city_info
    }

    return render(request, 'weather/index.html', context)  # по умолчанию все шаблоны
# ищутся в папке templates

