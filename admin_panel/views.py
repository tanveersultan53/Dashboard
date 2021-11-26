from django.shortcuts import render
from django.views.generic import ListView, CreateView, View
# Create your views here.


def TestView(request):
    return render(request=request,template_name="admin_panel/testing.html")


def RimshaView(request):
    return render(request=request,template_name="admin_panel/rimsha.html")