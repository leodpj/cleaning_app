from django.db import models
from clients.models import Client
from django.conf import settings

class Quote(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    professional = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("rejected", "Rejected")
    ], default="pending")
    created_at = models.DateTimeField(auto_now_add=True)
