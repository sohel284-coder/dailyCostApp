from datetime import date
from django.shortcuts import render

from costapp.models import MyCost

def index(request):
    today =  date.today()
    print(today)
   
    return render(request, 'index.html', {
        'today':today,
    })


