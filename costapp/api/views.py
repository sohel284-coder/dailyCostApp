from datetime import date
from datetime import datetime

from django.db.models import Sum, Max
from django.db.models.functions import Trunc

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.generics import get_object_or_404

from costapp.api.serializers import MyCostSerializer
from costapp.models import AddIncome, MyCost






class TodayMyCostAPIView(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, format=None):
        today = date.today()
        today_cost_list = MyCost.objects.filter(date_of_cost=today, user=request.user)
        print(today_cost_list)
        serializer = MyCostSerializer(today_cost_list, many=True)

        serializer_data = serializer.data
        today_total_cost = 0
        for data in serializer_data:
            today_total_cost = today_total_cost + data['amount_of_cost']


        income = AddIncome.objects.filter(month_name=datetime.now().month).values('income_amount').annotate(greatest=Max('income_amount')).values('greatest').aggregate(total=Sum('greatest'))
        print(income)


        context = {
            'today_cost_list':serializer.data,
            'today_total_cost':today_total_cost,
            'income':income,
        }   
       
        return Response(context, status=status.HTTP_200_OK)



    def post(self, request, format=None, ):
        today = date.today()
        today_cost_lists = MyCost.objects.filter(date_of_cost=today)
        
        data = request.data
        data['user'] = request.user.id
        total = data['amount_of_cost']
        try:
            for lst in today_cost_lists:
                print(lst['amount_of_cost'])
                total = total + lst['amount_of_cost']
                print(total)
        except:
            pass        

        data['daily_total_cost'] = total    

        serializer = MyCostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response('successfully save', status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SingleTodayCostAPIView(APIView):
    permission_classes = (permissions.AllowAny, )

    def get_single_cost(self, pk):
        cost_info = get_object_or_404(MyCost, pk=pk)
        return cost_info

    def get(self, request, pk, format=None):
        single_cost_info = self.get_single_cost(pk) 
        serializer = MyCostSerializer(single_cost_info)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        today = date.today()
        single_cost_info = self.get_single_cost(pk)
        data = request.data
        data['date_of_cost'] = today
        serializer = MyCostSerializer(single_cost_info, data=data, )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        single_cost_info = self.get_single_cost(pk)
        single_cost_info.delete()
        return Response('successfully Delete', status=status.HTTP_204_NO_CONTENT)


class CurrentMonthCostAPIView(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request):
        current_month = datetime.now().month
        current_month_cost_lists = MyCost.objects.filter(created_at__month=current_month, user=request.user)
        cmc_lists = current_month_cost_lists.filter().values('date_of_cost').order_by('-date_of_cost').annotate(total=Sum('amount_of_cost'))

        monthly_total_cost = 0

        for lst in cmc_lists:
            monthly_total_cost = monthly_total_cost + lst['total']
        
        context = {
            'cmc_lists':cmc_lists,
            'monthly_total_cost':monthly_total_cost,
            'current_month':current_month,
        }
        return Response(context, status=status.HTTP_200_OK)


class MonthlyCostAPIView(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, month):
        current_month = month
        print(current_month)
        try:
            current_month_cost_lists = MyCost.objects.filter(created_at__month=current_month, user=request.user)
        except:
            context = {}; 
            return Response(context, status=status.HTTP_200_OK) 
        cmc_lists = current_month_cost_lists.filter().values('date_of_cost').order_by('-date_of_cost').annotate(total=Sum('amount_of_cost'))

        monthly_total_cost = 0

        for lst in cmc_lists:
            monthly_total_cost = monthly_total_cost + lst['total']
        
        context = {
            'cmc_lists':cmc_lists,
            'monthly_total_cost':monthly_total_cost,
            'current_month':current_month,
        }
        return Response(context, status=status.HTTP_200_OK)


class ShowDetails(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, date_param):
        date_wise_cost_lists = MyCost.objects.filter(date_of_cost=date_param, user=request.user)
        serializer = MyCostSerializer(date_wise_cost_lists, many=True, )

        serializer_data = serializer.data
        date_wise_total_cost = 0

        for data in serializer_data:
            date_wise_total_cost = date_wise_total_cost + data['amount_of_cost']

        context = {
            'date_wise_cost_lists':serializer.data,
            'date_wise_total_cost':date_wise_total_cost
        } 
        return Response(context, status=status.HTTP_200_OK)


class UpdateDeleteDateWiseCost(APIView):
    permission_classes = (permissions.AllowAny, )

    def get_single_cost(self, pk):
        cost_info = get_object_or_404(MyCost, pk=pk)
        return cost_info

    def get(self, request, pk, format=None):
        single_cost_info = self.get_single_cost(pk) 
        serializer = MyCostSerializer(single_cost_info)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        single_cost_info = self.get_single_cost(pk)
        data = request.data

        data['date_of_cost'] = single_cost_info.date_of_cost
        serializer = MyCostSerializer(single_cost_info, data=data, )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        single_cost_info = self.get_single_cost(pk)
        single_cost_info.delete()
        return Response('successfully Delete', status=status.HTTP_204_NO_CONTENT)






"""
  costs = (current_month_cost_lists
            .annotate(day=Trunc('created_at', 'day'))
            .values('day')
            .annotate(greatest=Max('amount_of_cost'))
            .values('greatest')
            .aggregate(total=Sum('greatest'))
        )

        print(costs)
"""