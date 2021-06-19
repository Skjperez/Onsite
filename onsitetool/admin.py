from django.contrib import admin
from .models import ClientAssessment

# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    list_individual = (
        'id',
        'user', 
        'client_name', 
        'assessment_location', 
        'assessment_date', 
        'change_in_status', 
        'status_overview',
        'services_implemented',
        'services_overview', 
        'change_in_plan',
        'plan_overview',
        )
admin.site.register(ClientAssessment, ClientAdmin)