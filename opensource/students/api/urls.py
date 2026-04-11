from django.urls import path
from students.api.views import index, create, student_operartions
urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create'),
    path('<int:pk>', student_operartions, name='student_operartions'),
]