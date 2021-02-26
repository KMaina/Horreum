from django.db import models
from horreum.apps.authentication.models import User


class Product(models.Model):
    """class for products"""

    class Units(models.TextChoices):
        """Different units of measurements"""
        NONE = "NONE", "none"
        KG = "KG", "kg"
        L = "L", "l"
        PACKETS = "PACKETS", "packets"

    name = models.CharField(max_length=100, null=False, unique=True)
    quantity = models.IntegerField(default=0, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    UoM = models.CharField(max_length=50, choices=Units.choices, default=Units.NONE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
