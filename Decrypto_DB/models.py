from django.db import models


class Cryptocurrency(models.Model):
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)




