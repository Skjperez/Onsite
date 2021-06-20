from django.urls import path
from .views import CreateView, ReadView, ReviewView, DeleteView, UpdateView

urlpatterns = [
    path('create/', CreateView, name='create_onsite'),
    path('read/', ReadView, name='read_onsite'),
    path('<int:client_id>/', ReviewView, name='review_onsite'),
    path('<int:client_id>/delete/', DeleteView, name='delete_onsite'),
    path('<int:client_id>/update/', UpdateView, name='update_onsite'),
]