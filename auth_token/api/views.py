from django.shortcuts import render
from rest_framework import viewsets
from .seriallizer import StudenModelSerializer
from .models import Student


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudenModelSerializer

