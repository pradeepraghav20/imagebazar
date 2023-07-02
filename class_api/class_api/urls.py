from django.contrib import admin
from django.urls import include
from django.urls import path
from api import views
from rest_framework import routers

from api.views import StudentModelViewSet


routers=routers.DefaultRouter()
routers.register("studentapi",StudentModelViewSet,basename="studentapi")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(routers.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
    # path('studentapi/<int:pk>/', views.StudentAPI.as_view),


]
