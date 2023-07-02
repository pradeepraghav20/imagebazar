from django.shortcuts import render
from .models import Student
from .seriallizer import StudentSerializer
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework import status
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def stu_api(request,pk=None):
    if (request.method=='GET'):
        id=pk
        if id is not None:
            stu=Student.objects.get(id=id)
            studentserializer=StudentSerializer(stu)
            return Response(studentserializer.data)
            
        stu=Student.objects.all()
        studentserializer=StudentSerializer(stu,many=True)
        return Response(studentserializer.data)
    if (request.method=='POST'):
        studentserializer=StudentSerializer(data=request.data)
        if (studentserializer.is_valid()):
            studentserializer.save()
            return Response({"msg":"Data is added"})
        return Response(Serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if (request.method=='PUT'):
        id=pk
        stu=Student.objects.get(pk=id)
        studentserializer=StudentSerializer(stu,data=request.data)
        if (studentserializer.is_valid()):
            studentserializer.save()
            return Response({"msg":"Data is updated"})
        return Response(Serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if (request.method=='PATCH'):
        id=pk
        stu=Student.objects.get(pk=id)
        studentserializer=StudentSerializer(stu,data=request.data,partial=True)
        if (studentserializer.is_valid()):
            studentserializer.save()
            return Response({"msg":"Data is updated"})
        return Response(Serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        
    if (request.method=='DELETE'):
        id=pk
        stu=Student.objects.get(pk=id)
        stu.delete()
        return Response({"msg":"Data is Deleted successfully"})
    
    
        # return Response(Serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        

    


