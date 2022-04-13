from django.urls import path

from accountapp.views import login, signup, logout_user

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout_user, name='logout'),
]