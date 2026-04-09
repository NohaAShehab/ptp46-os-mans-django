
from django.contrib import admin
from django.urls import path, include

from departments.views import landing, index, CreateDepartmentView, show
app_name = 'departments'

urlpatterns = [
    # departments
    path('landing/', landing, name='landing'),
    path('index/',index , name='index' ),
    # path('create/',create , name='create'),
    path('create/', CreateDepartmentView.as_view(), name='create'),
    path('<int:id>', show, name='show'),

]
