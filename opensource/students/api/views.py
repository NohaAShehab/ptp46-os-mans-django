from rest_framework import status

from students.models import Student
# from django.http import JsonResponse
from students.api.serializers import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# def index(request):
#     students = Student.objects.all()
#
#     serialized_students = []
#     for student in students:
#         serialized_students.append({
#             'name': student.name,
#             'id': student.id
#         })
#
#     return JsonResponse({'students': serialized_students})
#
#
# def index(request):
#     students = Student.objects.all()
#     # send the data to the serilizer then return with the result
#     serialized_students = StudentSerializer(students, many=True)
#     print(serialized_students.data)
#     return JsonResponse(serialized_students.data, safe=False)


@api_view(['GET'])
def index(request):
    students = Student.objects.all()
    # send the data to the serilizer then return with the result
    serialized_students = StudentSerializer(students, many=True)
    print(serialized_students.data)
    # return JsonResponse(serialized_students.data, safe=False)
    return Response(serialized_students.data, status=status.HTTP_200_OK)

# create ?
@api_view(['POST'])
def create(request):
    print(request)
    print(request.data, type(request.data))
    # create object
    student = Student.objects.create(**request.data)
    # serialize the created object
    serialized_student = StudentSerializer(student)
    # accept data from form ?? ---> saveing as new object
    return Response(serialized_student.data, status=status.HTTP_201_CREATED)















