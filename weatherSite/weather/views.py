from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

def index(request):
    appid = '5f2887a8ea1643c8f436a30eeeec5f6e'
    # units=metric чтобы данные в цельсии
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    # условие сохранения данных (нового города)
#     if (request.method == 'POST'):
#         form = CityForm(request.POST)
#         form.save()
    
#     # очистка формы
#     form = CityForm()  

#     cities = City.objects.all()
#     all_cities = []

#     for city in cities:
#         res = requests.get(url.format(city)).json()
#         print(res)

#         # словарь с нужными мне данными из запроса, можно расширять
#         city_info = {
#             'city': city.name,
#             'temp': res["main"]["temp"],  # извлекаем данные из json запроса
#             'icon:': res["weather"][0]["icon"],
#             'description:': res["weather"][0]["description"]
#         }
#         print(city_info)

#         all_cities.append(city_info)

#     # передаем эти данные в шаблон index.html
#     context = {
#         'all_info': all_cities,
#         'form': form,
#     }

#     return render(request, 'weather/index.html', context)  # по умолчанию все шаблоны
# # ищутся в папке templates

    city = 'Munich'

    res = requests.get(url.format(city)).json()
    print(res)

    city_info = {
        'city': city,
        'temp': res["main"]["temp"],  # извлекаем данные из json запроса
        'icon': res["weather"][0]["icon"], # must come from the site
        'description': res["weather"][0]["description"]
    }
    print(city_info)

    # send info to context to send it to template
    context = {'city_info': city_info}

    return render(request, 'weather/index.html', context)

