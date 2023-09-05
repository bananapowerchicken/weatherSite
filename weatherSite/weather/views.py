from django.shortcuts import render

def index(request):
    appid = '5f2887a8ea1643c8f436a30eeeec5f6e'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=' + appid
    
    city = 'London'

    return render(request, 'weather/index.html')  # по умолчанию все шаблоны
# ищутся в папке templates

