from rest_framework import serializers
from app1.models import StudentInfo

# code here

class StudentInfoSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    father_name = serializers.CharField(max_length=100)
    email = serializers.EmailField()

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return StudentInfo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.father_name = validated_data.get('father_name', instance.father_name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
