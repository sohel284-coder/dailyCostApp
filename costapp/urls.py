from django.urls import path
from costapp.views import index
from costapp.api.views import TodayMyCostAPIView, SingleTodayCostAPIView, CurrentMonthCostAPIView, ShowDetails, UpdateDeleteDateWiseCost, MonthlyCostAPIView




urlpatterns = [
    path('', index, name='inddex'),

    path('api/today-cost-list/', TodayMyCostAPIView.as_view(), name='today_cost_list'),

    path('api/today-cost-list/<int:pk>/', SingleTodayCostAPIView.as_view(), name='today_cost_list'),

    path('api/current-month-cost-list/', CurrentMonthCostAPIView.as_view(), name='current_month_cost_list'),

    path('api/monthly-cost-list/<int:month>/', MonthlyCostAPIView.as_view(), name='monthly_cost_api_view'),


    path('api/show-details/<str:date_param>/', ShowDetails.as_view(), name='show_details'),

    path('api/update-date-wise-cost/<int:pk>/', UpdateDeleteDateWiseCost.as_view(), name='update-date-wise-cost'),

]