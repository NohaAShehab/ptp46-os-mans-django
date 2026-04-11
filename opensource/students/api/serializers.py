
from rest_framework import serializers


class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    age = serializers.IntegerField()
    email = serializers.EmailField()
    image = serializers.ImageField()
    gender = serializers.CharField()
    salary = serializers.IntegerField()





