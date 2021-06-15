from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    visit_location = models.CharField(max_length=50)
    date = models.DateField()

    def __str__(self):
        return self.name #name to be shown when called
