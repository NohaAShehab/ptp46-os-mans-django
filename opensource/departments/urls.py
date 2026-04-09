
from django.contrib import admin
from django.urls import path, include

from departments.views import landing, index, create, show

urlpatterns = [
    # departments
    path('landing/', landing, name='departments.landing'),
    path('index/',index , name='departments.index' ),
    path('create/',create , name='departments.create'),
    path('<int:id>', show, name='departments.show'),

]
