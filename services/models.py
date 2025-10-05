from django.db import models
from django.conf import settings
from clients.models import Client

class Service(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    professional = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[
        ("scheduled", "Scheduled"),
        ("done", "Done"),
        ("canceled", "Canceled")
    ], default="scheduled")
