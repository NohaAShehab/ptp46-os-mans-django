from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse

from students.forms import StudentForm
from students.models import Student
# Create your views here.

def hello_world(request):
    print(f"request: {request}")
    # handle http request  --> request
    # return with http response
    return HttpResponse("Hello World")



students = [
    {"id": 1, "name": "Mohamed Waleed", "salary": 150000, "image": "pic1.jpeg"},
    {"id": 2, "name": "Karim", "salary": 20000, "image": "pic2.jpeg"},
    {"id": 3, "name": "Abdelhamid", "salary": 30000, "image": "pic3.jpeg"},
]
#
# def index(request):
#     return HttpResponse(students)

#
# def profile(request, id):
#     try:
#         id = int(id)
#         student  = filter(lambda std:std['id'] == id, students) # filter object
#         print(student)
#         student = list(student)
#         print(student)
#         if student:
#             return HttpResponse(student[0])
#     except:
#         return HttpResponse("Not found")
#
#     return HttpResponse("Not found")


#
# def profile(request, id ):
#     # <int:id> === do the required casting
#     student  = filter(lambda std:std['id'] == id, students) # filter object
#     print(student)
#     student = list(student)
#     print(student)
#     if student:
#         return HttpResponse(student[0])
#
#     return HttpResponse("Not found")


def index(request):
    # I need to get students from the database
    students=  Student.objects.all()
    print(students)
    return render(request, "students/index.html",
                  context={'students': students} )




# def profile(request, id ):
#     student = Student.objects.filter(id=id)
#     print(student)
#     if student:
#         return render(request, "students/show.html", context={'student': student[0]})
#
#     return HttpResponse("Not found")


# def profile(request, id ):
#     student = Student.objects.get(id=id) # one object
#     print(student)
#     if student:
#         return render(request, "students/show.html", context={'student': student})
#
#     return HttpResponse("Not found")


def profile(request, id ):
    student = get_object_or_404(Student, pk=id)
    print(student)
    return render(request, "students/show.html", context={'student': student})


# def create(request):
#     # I need django to create html fields
#     form = StudentForm()
#     if request.method == "POST":
#         # you can use form object to validate data ... ?? save cleaned_data ?
#
#         form = StudentForm(request.POST)
#
#         print(request.POST) # container --> have the data
#         student = Student()
#         student.name = request.POST["name"]
#         student.email = request.POST["email"]
#         student.salary = request.POST["salary"]
#         student.image = request.POST["image"]
#         student.gender = request.POST["gender"]
#         student.age = request.POST["age"]
#         student.save()
#         url = reverse("students.profile", args=[student.id])
#         return redirect(url)
#         # return  HttpResponse("Post request received")
#         return
#     return render(request, "students/create.html",
#                   context={'form': form})


def create(request):
    # I need django to create html fields
    form = StudentForm()
    if request.method == "POST":
        # you can use form object to validate data ... ?? save cleaned_data ?
        form = StudentForm(request.POST)
        print(request.POST) # container --> have the data
        if form.is_valid():  # check validation rules defined in the forms.py
            student = Student()
            print(form.cleaned_data)
            student.name = form.cleaned_data["name"]
            student.salary = form.cleaned_data["salary"]
            student.image = form.cleaned_data["image"]
            student.age = form.cleaned_data["age"]
            student.email = form.cleaned_data["email"]
            student.gender = form.cleaned_data["gender"]
            student.save()
            url = reverse("students.profile", args=[student.id])
            return redirect(url)
    return render(request, "students/create.html",
                  context={'form': form})




