
from django.contrib import admin
from django.urls import path, include

from departments.views import  landing, index

urlpatterns = [
    # departments
    path('landing/', landing, name='departments.landing'),
    path('index/',index , name='departments.index' ),

]
