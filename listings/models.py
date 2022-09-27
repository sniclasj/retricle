from django.db import models
from athletes.models import Athlete


class Discipline(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Listing(models.Model):
    lister = models.ForeignKey(
        Athlete, null=False, blank=False, on_delete=models.CASCADE)
    discipline = models.ForeignKey(
        'Discipline', null=False, blank=False, on_delete=models.CASCADE)
    condition = models.ForeignKey(
        'Condition', null=False, blank=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Condition(models.Model):
    wear = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.wear
