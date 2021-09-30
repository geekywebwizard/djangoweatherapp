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
        api_request = requests.get("https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode="+zipcode+"&date=2021-09-30&distance=50&API_KEY=B176FE17-0119-4E2F-A142-5F74A516CF97")
            
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
    
