from django.shortcuts import render
from .models import *
from rest_framework.views import APIView
from .seriallizer import *
from rest_framework.response import Response
# Create your views here.

class HandleFileUpload(APIView):
    def post(self,request):
        try:

            data=request.data
            serializer=FileListSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                        'status' : 200,
                        'message' : 'files uploaded successfully',
                        'data' : serializer.data
                    })
                
            return Response({
                    'status' : 400,
                    'message' : 'somethign went wrong',
                    'data'  : serializer.errors
                })
        except Exception as error:
            print(error)
