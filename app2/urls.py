from app2.views import *
from django.urls import path

app_name = 'connect2'

urlpatterns=[
  path('page6/',page6,name='page6'),
  path('page7/',page7,name='page7'),
  path('page8/',page8,name='page8'),
  path('page9/',page9,name='page9'),
  path('page10/',page10,name='page10'),
]