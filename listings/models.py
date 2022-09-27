from django.db import models
from django.contrib.auth.models import User


class Discipline(models.Model):
    listing = models.ForeignKey(
        'Listings', null=False, blank=False, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Listings(models.Model):
    lister = models.ForeignKey(
        'User', null=False, blank=False, on_delete=models.CASCADE)
    discipline = models.ForeignKey(
        'Discipline', null=False, blank=False, on_delete=models.SET_NULL)
    condition = models.ForeignKey(
        'Condition', null=False, blank=False, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Condition(models.Model):
    listing = models.ForeignKey(
        'Listings', null=False, blank=False, on_delete=models.SET_NULL)
    wear = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.wear