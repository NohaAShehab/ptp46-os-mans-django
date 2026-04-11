from django.db import models

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    max_grade = models.IntegerField(default=100)
    cover = models.ImageField(upload_to='courses/covers/' , null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True , blank=True)

    def __str__(self):
        return f'{self.name}'


