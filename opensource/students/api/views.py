from traceback import print_stack

from rest_framework import status

from students.models import Student
# from django.http import JsonResponse
from students.api.serializers import StudentSerializer, StudentModelSerializer
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
# @api_view(['POST'])
# def create(request):
#     print(request)
#     print(request.data, type(request.data))
#     # create object
#     student = Student.objects.create(**request.data)
#     # serialize the created object
#     serialized_student = StudentSerializer(student)
#     # accept data from form ?? ---> saveing as new object
#     return Response(serialized_student.data, status=status.HTTP_201_CREATED)



# send data to the serializer
"""

{'id': [ErrorDetail(string='This field is required.', code='required')], 
'image': [ErrorDetail(string='No file was submitted.', code='required')], 
'salary': [ErrorDetail(string='This field is required.', code='required')]}
"""
@api_view(['POST'])
def create(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        # student= Student.objects.create(**serializer.validated_data)
        # serialized_student = StudentSerializer(student)
        student = serializer.create(**serializer.validated_data)
        # serialized_student = StudentSerializer(student)
        return Response(student.data, status=status.HTTP_201_CREATED)
    else:
        print(serializer.errors)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['PUT', 'DELETE', 'GET'])
def student_operartions(request, pk):
    student = Student.objects.get(pk=pk)
    student_serializer = StudentSerializer(student)

    if request.method == 'PUT':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            student_serializer.update(student, **serializer.validated_data)
            return Response(student_serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        student.delete()
        return Response({"deleted": "ok"},status=status.HTTP_204_NO_CONTENT)

    else:
        return Response(student_serializer.data, status=status.HTTP_200_OK)






###########################
@api_view(['GET', 'POST'])
def students(request):
    if request.method == 'GET':
        students = Student.objects.all()
        students = StudentModelSerializer(students, many=True)
        print(students.data)

        return Response(students.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        # send data to the serializer so it will create new object
        serializer = StudentModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create(**serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)























