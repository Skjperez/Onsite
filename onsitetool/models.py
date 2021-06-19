from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ClientAssessment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=50)
    assessment_location = models.CharField(max_length=50)
    assessment_date = models.DateField()
    change_in_status = models.BooleanField()
    status_overview = models.TextField()
    services_implemented = models.BooleanField()
    services_overivew = models.TextField()
    change_in_plan = models.BooleanField()
    plan_overview= models.TextField()

    def __str__(self):
        return self.name #name to be shown when called
