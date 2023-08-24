from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Notes
from .serializer import NotesModelSerializer
from rest_framework import viewsets
from rest_framework import authentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated



class NotesModelViewSet(viewsets.ModelViewSet):
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]
    queryset=Notes.objects.all()
    serializer_class=NotesModelSerializer


# class NoteList(generics.ListCreateAPIView):
#     queryset = Notes.objects.all()
#     serializer_class = NotesModelSerializer
# class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Notes.objects.all()
#     serializer_class = NotesModelSerializer

