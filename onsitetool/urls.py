from django.urls import path
from .views import CreateView, ReadView, ReviewView

urlpatterns = [
    path('create/', CreateView, name='create_onsite'),
    path('read/', ReadView, name='read_onsite'),
    path('<int:client_id>/', ReviewView, name='review_onsite')
]