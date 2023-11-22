from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def page1(request):
  return HttpResponse('<h1>This is http string as response.</h1>')

def page2(request):
  d={'string':'This page is for jinja printing tag.'}
  return render(request,'page2.html',context=d)

def page3(request):
  d={'a':100,'b':300}
  return render(request,'page3.html',context=d)

def page4(request):
  d={'string':'This page is for looping jinja operational tag.'}
  return render(request,'page4.html',context=d)

def page5(request):
  return render(request,'page5.html')