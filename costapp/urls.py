from django.urls import path
from costapp.views import index
from costapp.api.views import TodayMyCostAPIView, SingleTodayCostAPIView




urlpatterns = [
    path('', index, name='inddex'),

    path('api/today-cost-list/', TodayMyCostAPIView.as_view(), name='today_cost_list'),

    path('api/today-cost-list/<int:pk>/', SingleTodayCostAPIView.as_view(), name='today_cost_list'),

]