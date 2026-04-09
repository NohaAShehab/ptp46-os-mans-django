
from django.urls import path

from students.views import hello_world, index, profile, create, CreateStudentView

urlpatterns = [
    # students
    path('hello',hello_world, name='students.hello'),
    path('index/', index, name='students.index'),
    # path('profile/<id>', profile, name='profile'),
    path('profile/<int:id>', profile, name='students.profile'),
    path('create',create, name='students.create' ),
    path("create/forms", CreateStudentView.as_view(), name="students.create_forms"),
]
