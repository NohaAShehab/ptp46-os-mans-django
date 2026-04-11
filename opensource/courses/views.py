from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import  ListView, DetailView

from courses.forms import CourseForm
from courses.models import Course


# Create your views here.
#
# def index(request):
#     return render(request, 'courses/index.html')


## generic view to create new course

class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'courses/create.html'
    success_url = '/courses/index'
    
    # override post functionality




class CourseListView(ListView):
    model = Course
    template_name = 'courses/index.html'
    # context_object_name = 'courses'


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/show.html'
    pk_url_kwarg = "id"












