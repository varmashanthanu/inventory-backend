# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Administrator'),
        ('warehouse_manager', 'Warehouse Manager'),
        ('calibration_specialist', 'Calibration Specialist'),
        ('inventory_clerk', 'Inventory Clerk'),
        ('purchasing_agent', 'Purchasing Agent'),
        ('quality_control_inspector', 'Quality Control Inspector'),
        ('finance_officer', 'Finance Officer'),
        ('mechanic', 'Mechanic'),
        ('warehouse_operator', 'Warehouse Operator'),
        ('maintenance_planner', 'Maintenance Planner'),
    ]

    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.username


class RevokedToken(models.Model):
    """
    Stores revoked access tokens so they cannot be reused after logout.
    """
    token = models.CharField(max_length=500, unique=True)  # Store the full token
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp of when revoked

    def __str__(self):
        return self.token