from django.db import models
from django.utils import timezone

import random
import string


def generer(nb_caracters):
    caracters = string.ascii_letters + string.digits
    alea = [random.choice(caracters) for _ in range(nb_caracters)]
    return alea


# Create your models here.
class MiniUrl(models.Model):
    url = models.URLField(unique = True)
    code = models.CharField(max_length = 6, unique = True)
    creation_date = models.DateTimeField(default = timezone.now)
    pseudo = models.CharField(max_length = 30)
    nb_access = models.IntegerField(default = 0)

    def __str__(self):
        return self.url

    def save(self, *args, **kwargs):
        if len(self.code)==0 :
            self.code = generer(6)
        super().save(*args, **kwargs)
