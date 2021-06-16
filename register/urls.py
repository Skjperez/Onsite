from django.urls import path 
from .views import UserLogout, Signup, UserLogin

urlpatterns = [

    path('logout/', UserLogout, name='logout'),
    path('signup/', Signup, name='signup'),
    path('login/', UserLogin, name='login'),
]