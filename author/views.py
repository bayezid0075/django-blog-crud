from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def reg(request): 
   data = {
       "title": "Register in Django website",
       "loged": True
   }
   return render(request,"abc/index.html", context=data)

def login(req): 
    profile = [
       { "id": random.randint(2,99),
         "name": "color",
         "value": "red",
         "price": 10
       },
       { "id": random.randint(2,99),
           "name": "size",
           "value": "XL",
           "price": 13
       },
       { "id": random.randint(2,99),
           "name": "categories",
            "value": "ready to use production",
            "price": 25
       }

    ]
    return render(req, 'abc/login.html', {"data": profile})


