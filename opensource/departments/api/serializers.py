


from rest_framework import serializers



class DepartmentSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=100)
    logo = serializers.ImageField(allow_null=True, required=False)
    created_at = serializers.DateTimeField( read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
