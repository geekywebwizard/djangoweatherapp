from io import RawIOBase
from django.shortcuts import render
from requests.sessions import Request
from datetime import date, datetime

# Create your views here.
def home(request):
    
    import json
    import requests

    if request.method  == "POST":
        zipcode = request.POST["zipcode"]
        today = datetime.today
        api_request = requests.get("https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode="+zipcode+"&date=&distance=50&API_KEY=B176FE17-0119-4E2F-A142-5F74A516CF97")
        
            
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error ..."
        
        return render(request, 'home.html' , {'api': api} )
    else:

        api_request = requests.get("https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=35242&date=2021-09-30&distance=25&API_KEY=B176FE17-0119-4E2F-A142-5F74A516CF97")
            
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error ..."
        
        return render(request, 'home.html' , {'api': api} )
 
 


        

def about(request):
    return render(request, 'about.html', {})

def contact(request):
    return render(request, 'contact.html', {})


def openweather(request):

    import json
    import requests

    if request.method  == "POST":
        zipcode_open = request.POST["zipcode_open"]
        country_open = request.POST["country_open"]


        open_api_request = requests.get("http://api.openweathermap.org/data/2.5/weather?zip="+zipcode_open+","+country_open+"&appid=0e4c021e29f746ddd6e9c1a8764f2a0f")
        
        open_api = json.loads(open_api_request.content)
        
        return render(request, 'openweather.html' , {'open_api': open_api} )


    else:

        open_api_request = requests.get("http://api.openweathermap.org/data/2.5/weather?zip=585105,IN&appid=0e4c021e29f746ddd6e9c1a8764f2a0f")
        
        open_api = json.loads(open_api_request.content)
        
        return render(request, 'openweather.html' , {'open_api': open_api} )

    
    
