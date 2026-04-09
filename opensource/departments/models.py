from django.db import models
from django.shortcuts import get_object_or_404, reverse

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    active = models.BooleanField(default=True)
    logo = models.ImageField(upload_to='departments/logos/', null=True, blank=True)

    def __str__(self):
        return f"{self.name}({self.id})"


    @classmethod
    def get_active_departments(cls):
        departments = cls.objects.filter(active=True).order_by('-created_at')
        return departments


    @classmethod
    def get_dept_by_id(cls , id):
        return get_object_or_404(Department , pk=id)


    @property
    def show_url(self):
        url = reverse("departments:show", args=[self.id])
        return url