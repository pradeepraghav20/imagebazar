from django.shortcuts import render
import requests
from rest_framework.parsers import JSONParser
from .models import Student
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
import io
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def student_data(request):
    if request.method=='GET':
        json_data=request.body
        steam=io.BytesIO(json_data)
        python_data=JSONParser().parse(steam)
        id=python_data.get('id',None)

        if id is not None:
            stu_data=Student.objects.get(id=id)
            serializer=StudentSerializer(stu_data)
            json_data= JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type="application/json")
        else:
            stu_data=Student.objects.all()
            serializer=StudentSerializer(stu_data,many=True)
            json_data= JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type="application/json")
    
        
    if request.method=="POST":
        json_data=request.body
        steam=io.BytesIO(json_data)
        python_data=JSONParser().parse(steam)
        serialize_data=StudentSerializer(data=python_data)
        if serialize_data.is_valid():
            serialize_data.save()
            res={'msg':'data has been created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type="application/json")
        

    if request.method == 'PUT':
       json_data = request.body
       stream = io.BytesIO(json_data)
       pythondata = JSONParser().parse(stream)
       id = pythondata.get('id')
       stu = Student.objects.get(id=id)
       serializer = StudentSerializer(stu, data=pythondata, partial=True)
       if serializer.is_valid():
          serializer.save()
          res = {'msg':'Data Updated !!'}
          json_data = JSONRenderer().render(res)
          return HttpResponse(json_data, content_type='application/json')
       


        
    
        

        


            







    
