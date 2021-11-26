from django.urls import path
from .views import TestView,RimshaView

urlpatterns = [
    path('test-temp/', TestView, name='test-temp'),
    path('rimsha/',RimshaView,name='rimsha')
]