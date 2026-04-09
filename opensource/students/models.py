from random import choices

from django.db import models
from django.shortcuts import reverse

# Create your models here.


class Student(models.Model):
    # model ? name, email, gender, image, age
    #by default all fields --> not null until you say null=True
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(max_length=100, null=True, unique=True)
    image = models.ImageField(upload_to='students/images', null=True, blank=True)
    gender = models.CharField(choices=[('m', 'Male'), ('f', 'Female')], max_length=1, default='m')
    salary = models.IntegerField(default=5000, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


    def __str__(self):
        return f'{self.name}({self.id})'


    @property
    def show_url(self):
        return  reverse("students.profile", args=[self.id])

    @property
    def image_url(self):
        if self.image:
            return f'{self.image.url}'

        else:
            return f'/media/students/images/default.png'