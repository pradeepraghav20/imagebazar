from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=50)
    city=serializers.CharField(max_length=50)
    roll=serializers.CharField(max_length=50)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    

    def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.roll=validated_data.get('roll',instance.roll)
        instance.city=validated_data.get('name',instance.city)
        instance.save()
        return instance
    

    

    def __str__(self):
        return self.name
    
