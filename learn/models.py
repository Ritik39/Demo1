import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


class Register(models.Model):

    designation = (('Developer', 'Developer'),
                   ('Senior Developer', 'Senior Developer'),
                   ('Project Manager', 'Project Manager'))

    name = models.CharField(max_length=255)
    designation = models.CharField(choices=designation, max_length=255)
    registered_on = models.DateTimeField(default=datetime.datetime.now())

    class Meta:
        db_table = 'register'
        verbose_name = 'Register'
        verbose_name_plural = 'Register'
