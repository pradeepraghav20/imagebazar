from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .seriallizer import StudentSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
# Create your views here

# class StudentAPI(APIView):
#  def get(self, request, pk=None, format=None):
#   id = pk
#   if id is not None:
#    stu = Student.objects.get(id=id)
#    serializer = StudentSerializer(stu)
#    return Response(serializer.data)

#   stu = Student.objects.all()
#   serializer = StudentSerializer(stu, many=True)
#   return Response(serializer.data)

#  def post(self, request, format=None):
#   serializer = StudentSerializer(data=request.data)
#   if serializer.is_valid():
#    serializer.save()
#    return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
#   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#  def put(self, request, pk, format=None):
#   id = pk
#   stu = Student.objects.get(pk=id)
#   serializer = StudentSerializer(stu, data=request.data)
#   if serializer.is_valid():
#    serializer.save()
#    return Response({'msg':'Complete Data Updated'})
#   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#  def patch(self, request, pk, format=None):
#   id = pk
#   stu = Student.objects.get(pk=id)
#   serializer = StudentSerializer(stu, data=request.data, partial=True)
#   if serializer.is_valid():
#    serializer.save()
#    return Response({'msg':'Partial Data Updated'})
#   return Response(serializer.errors)

#  def delete(self, request, pk, format=None):
#   id = pk
#   stu = Student.objects.get(pk=id)
#   stu.delete()
#   return Response({'msg':'Data Deleted'})


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    # authentication_classes=[BasicAuthentication]
    # permission_classes=[IsAuthenticated]
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]
    throttle_classes=[UserRateThrottle,AnonRateThrottle]
    


# class StudentModelViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
