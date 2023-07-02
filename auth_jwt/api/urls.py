from .views import HelloView
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    
	path('hello/', HelloView.as_view(),name="helloviw"),
]
