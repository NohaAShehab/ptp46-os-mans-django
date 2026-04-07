
from django.contrib import admin
from django.urls import path, include

from departments.views import  landing

urlpatterns = [
    # departments
    path('landing/', landing, name='departments.landing')

]
