from random import choices

from django.contrib.gis.admin import options
from django.db import models

# Create your models here.


class Student(models.Model):
    # model ? name, email, gender, image, age
    #by default all fields --> not null until you say null=True
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(max_length=100, null=True, unique=True)
    image = models.CharField(max_length=100, null=True)
    gender = models.CharField(choices=[('m', 'Male'), ('f', 'Female')], max_length=1, default='m')
    salary = models.IntegerField(default=5000, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


    def __str__(self):
        return f'{self.name}({self.id})'