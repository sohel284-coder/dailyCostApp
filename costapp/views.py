from datetime import date
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from costapp.models import MyCost


@login_required(login_url='login')
def index(request):
    print(request.user)
    today =  date.today()
    print(today)
   
    return render(request, 'index.html', {
        'today':today,
        'username':request.user,
    })





