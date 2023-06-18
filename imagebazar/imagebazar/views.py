from django.http import HttpResponse
import requests
from django.shortcuts import render

def show_about_page(request):
    name='pradeepraghav'
    link='githun/pradeepraghav'
    data={
        'name':name,
        'link':link
    }
    return render(request,"about.html",data)

def show_home_page(request):
    return render(request,"home.html",)
