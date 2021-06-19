from django.urls import path
from .views import CreateView, ReadView

urlpatterns = [
    path('create/', CreateView, name='create_onsite'),
    path('read/', ReadView, name='read_onsite'),
]