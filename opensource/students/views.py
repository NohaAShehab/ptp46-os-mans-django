from django.shortcuts import render
from django.http import HttpResponse

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
    # return HttpResponse(students)
    # send the students to the html page  --> dynamic content
    # return template index.html
    return render(request, "students/index.html",
                  context={'students': students} )




def profile(request, id ):
    # <int:id> === do the required casting
    student  = filter(lambda std:std['id'] == id, students) # filter object
    print(student)
    student = list(student)
    print(student)
    if student:
        return render(request, "students/show.html", context={'student': student[0]})

    return HttpResponse("Not found")






