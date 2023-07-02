from django.contrib import admin
from django.urls import path
from enroll import views
from rest_framework import routers
from django.urls import include
from enroll.api import views
from enroll.api.serializers import StudentSerializers

routers=routers.DefaultRouter()
routers.register("studentapi",views.StudentViewSet,basename="stuapi")


urlpatterns = [
    path('', include(routers.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
 ]
  
