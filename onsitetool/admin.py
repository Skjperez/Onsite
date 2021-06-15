from django.contrib import admin
from .models import Client

# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    list_individual = (
        'user', 'name', 'visit_location', 'date',
        )
admin.site.register(Client, ClientAdmin)