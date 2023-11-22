from app1.views import *
from django.urls import path

app_name = 'connect1'

urlpatterns=[
  path('page1/',page1,name='page1'),
  path('page2/',page2,name='page2'),
  path('page3/',page3,name='page3'),
  path('page4/',page4,name='page4'),
]