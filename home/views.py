from django.shortcuts import render, HttpResponse
from django.template import loader
import requests
import json
from datetime import datetime
from home.models import Contact
from django.contrib import messages


import requests

  
    
# Create your views here.
# def index(request):
   
#     template=loader.get_template('index.html')
#     return HttpResponse(template.render())
def index(request):
    context={
    #   'date':datetime.today().time
    }
    category = 'fitness'
    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    response = requests.get(api_url, headers={'X-Api-Key': 'SokxODhRWmFdyPrOwnp26Q==2fKVTNa1wV8gdTRG'})
    data=response.json()
    if response.status_code == requests.codes.ok:
        for i in data:
            x=i['quote']   
    return render(request,"index.html",{'x':x})
def service(request):
    
    return render(request,"service.html")
def about(request):
    if request.method =="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name, email=email, phone=phone, desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been Submitted!")
    return render(request,"About.html")


def food(request):
    import requests
    import json
    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(
            api_url + query, headers={'X-Api-Key': 'SokxODhRWmFdyPrOwnp26Q==2fKVTNa1wV8gdTRG'})

        try:
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api = "oops! There was an error"
            print(e)
        
        return render(request, 'food.html', {'api': api})
    else:
        return render(request, 'food.html', {'query': 'Enter a valid query'})