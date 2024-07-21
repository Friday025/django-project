from django.shortcuts import render

import json
import urllib.request
# Create your views here.
def index(request):
    data = {}
    if request.method == 'POST':
        city = request.POST['city']

        API_KEY = "afe73c4fde62371c0a9a68ac28fd8693"

        source = urllib.request.urlopen(F"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}")
        data_list = json.load(source)

        data = {
            'city': data_list['name'],
            'country': data_list['sys']['country'],
            'temperature': data_list['main']['temp'] - 273.15,
            'description': data_list['weather'][0]['description'],
            'pressure' : data_list['main']['pressure'],
            'humidity' : data_list['main']['humidity'],
            'Feels_like' : data_list['main']['feels_like'] -273.15,
        }

       
        print(data)
   

    return render(request, 'main/index.html',data)
