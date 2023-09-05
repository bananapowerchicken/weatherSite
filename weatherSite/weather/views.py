from django.shortcuts import render

def index(request):
    return render(request, 'weather/index.html')  # по умолчанию все шаблоны
# ищутся в папке templates

