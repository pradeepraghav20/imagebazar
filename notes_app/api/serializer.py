from rest_framework import serializers
from .models import Notes

class NotesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Notes
        fields = ('id', 'title', 'text')



