from datetime import date

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.generics import get_object_or_404

from costapp.api.serializers import MyCostSerializer
from costapp.models import MyCost



class TodayMyCostAPIView(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, format=None):
        today = date.today()
        today_cost_list = MyCost.objects.filter(date_of_cost=today)
        print(today_cost_list)
        serializer = MyCostSerializer(today_cost_list, many=True)

        serializer_data = serializer.data
        today_total_cost = 0
        for data in serializer_data:
            today_total_cost = today_total_cost + data['amount_of_cost']

        context = {
            'today_cost_list':serializer.data,
            'today_total_cost':today_total_cost
        }   
       
        return Response(context, status=status.HTTP_200_OK)



    def post(self, request, format=None, ):
        today = date.today()
        today_cost_lists = MyCost.objects.filter(date_of_cost=today)
        
        data = request.data
        data['date_of_cost'] = today
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
