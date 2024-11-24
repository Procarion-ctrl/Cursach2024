from django.db import models
from django.contrib.auth.models import User

class Investment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)  # crypto, stock, deposit, or point investment
    asset_name = models.CharField(max_length=100, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    value_usd = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    annual_rate = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)  # For deposits
    description = models.TextField(blank=True, null=True)  # For point investments
    created_at = models.DateTimeField(auto_now_add=True)
