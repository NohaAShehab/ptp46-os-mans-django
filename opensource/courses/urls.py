from django.urls import path

from courses.views import CourseListView, CourseCreateView, CourseDetailView

app_name = 'courses'
urlpatterns = [
    path('index', CourseListView.as_view(), name='index'),
    path('create', CourseCreateView.as_view(), name='create'),
    path('<int:id>', CourseDetailView.as_view(), name='detail'),

]