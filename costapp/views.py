from datetime import date
from datetime import datetime
from django.db.models import Sum, Max
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from costapp.models import MyCost, AddIncome


@login_required(login_url='login')
def index(request):
    today =  date.today()
    current_month = datetime.now().month
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    current_month_name = months[current_month - 1]
    income = AddIncome.objects.filter(month_name=datetime.now().month).values('income_amount').annotate(greatest=Max('income_amount')).values('greatest').aggregate(total=Sum('greatest'))
    print(income)

    try:
        current_month_cost_lists = MyCost.objects.filter(created_at__month=current_month, user=request.user)
    except:
        context = {}; 
        return JsonResponse(context)

    cmc_lists = current_month_cost_lists.filter().values('date_of_cost').order_by('-date_of_cost').annotate(total=Sum('amount_of_cost'))

    monthly_total_cost = 0

    for lst in cmc_lists:
        monthly_total_cost = monthly_total_cost + lst['total']
    
    print(monthly_total_cost)

    balance = income['total'] - monthly_total_cost
    print(balance)
    return render(request, 'index.html', {
        'today':today,
        'username':request.user,
        'income':income['total'],
        'balance':balance,
        'current_month':current_month_name
    })





