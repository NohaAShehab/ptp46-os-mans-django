from django.shortcuts import render, reverse ,redirect
from django.http import HttpResponse, HttpResponseRedirect

from departments.forms import DepartmentForm
from departments.models import Department

# Create your views here.


def landing(request):
    # return HttpResponse("Landing Page")
    return render(request, 'departments/index.html')


# each url needs a view ?? to handle the request

def index(request):
    # departments = Department.objects.filter(active=True)
    departments = Department.get_active_departments()
    return render(request, 'departments/index.html', context={'departments': departments})




# create =--> define funciton of create

def create(request):
    form = DepartmentForm()
    if request.method == 'POST':
        form = DepartmentForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            active = form.cleaned_data['active']
            logo = form.cleaned_data['logo']
            department = Department(
                name=name,
                description=description,
                active=active,
                logo=logo
            )
            department.save()
            # return HttpResponse("Department created successfully")
            # redirect to the show page >>>
            url = reverse("departments.show", args=[department.id])
            print(url)
            # return HttpResponse("Department created successfully")
            return redirect(url)


    return render(request, 'departments/create.html',
                  context={'form': form})


# def create(request):
#     form = DepartmentForm()
#     if request.method == 'POST':
#         form = DepartmentForm(request.POST, request.FILES)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             description = form.cleaned_data['description']
#             active = form.cleaned_data['active']
#             logo = form.cleaned_data['logo']
#             department = Department(
#                 name=name,
#                 description=description,
#                 active=active,
#                 logo=logo
#             )
#             department.save()
#             return render(request, 'departments/show.html', context={'department': department})
#
#
#     return render(request, 'departments/create.html',
#                   context={'form': form})






def show(request, id):
    department = Department.get_dept_by_id(id)

    return render(request, 'departments/show.html', context={'department': department})








