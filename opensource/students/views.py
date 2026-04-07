from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello_world(request):
    print(f"request: {request}")
    # handle http request  --> request
    # return with http response
    return HttpResponse("Hello World")



students = [
    {"id": 1, "name": "Mohamed Waleed", "salary": 150000},
    {"id": 2, "name": "Karim", "salary": 20000},
    {"id": 3, "name": "Abdelhamid", "salary": 30000},
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



def profile(request, id ):
    # <int:id> === do the required casting
    student  = filter(lambda std:std['id'] == id, students) # filter object
    print(student)
    student = list(student)
    print(student)
    if student:
        return HttpResponse(student[0])

    return HttpResponse("Not found")


def index(request):
    # return HttpResponse(students)
    # return template index.html
    return render(request, "students/index.html")










