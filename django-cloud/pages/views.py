from django.shortcuts import render
from django.http import HttpResponse
from .models import TodoListItem 
from django.http import HttpResponseRedirect 
from django.shortcuts import render

def homePageView(request):
    return HttpResponse("Hello, World!")
  
# Create your views here.
