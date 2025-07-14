from django.db import models


class Cryptocurrency(models.Model):
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)


class Wallet(models.Model):
    address = models.CharField(max_length=255, unique=True)
    owner = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


class Asset(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='assets')
    crypto = models.ForeignKey(Cryptocurrency, on_delete=models.CASCADE, related_name='assets')
    amount = models.DecimalField(max_digits=20, decimal_places=8)

