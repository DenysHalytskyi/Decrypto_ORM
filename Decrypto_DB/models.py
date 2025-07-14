from django.db import models


class Cryptocurrency(models.Model):
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)


class Wallet(models.Model):
    address = models.CharField(max_length=255, unique=True)
    owner = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


