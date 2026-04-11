from markdown.extensions.toc import unique
from rest_framework import serializers

from departments.models import Department
from students.models import Student
from departments.api.serializers import DepartmentSerializer



class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    age = serializers.IntegerField()
    email = serializers.EmailField()
    image = serializers.ImageField(allow_null=True, required=False)
    gender = serializers.CharField()
    salary = serializers.IntegerField(allow_null=True, required=False)
    department_id = serializers.IntegerField(allow_null=True, required=False)
    department_name = serializers.CharField(required=False, read_only=True, source='department')
    # use dept. serializer
    department = DepartmentSerializer(read_only=True)


    def validate_email(self, value):
        email = value
        if Student.objects.filter(email=email).exists():
            raise serializers.ValidationError("Email already exists")
        return email


    def validate_department_id(self, value):
        department_id = value
        if Student.objects.filter(department_id=department_id).exists():
            return department_id
        raise serializers.ValidationError("Department id does not exist")


    def update(self, instance, **validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.email = validated_data.get('email', instance.email)
        instance.image = validated_data.get('image', instance.image)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.salary = validated_data.get('salary', instance.salary)
        instance.department_id = validated_data.get('department_id', instance.department_id)

        instance.save()
        return instance


    def create(self, **validated_data):
        student = Student.objects.create(**validated_data)
        student.save()
        return StudentSerializer(student)





