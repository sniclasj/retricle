from django.db import models
from django.contrib.auth.models import User


class Athlete(models.Model):
    athlete = models.OneToOneField('User', on_delete=models.CASCADE)
    is_seller = models.BooleanField(
        verbose_name='Is Seller?', null=False, default=False)

    def __str__(self):
        return self.athlete
