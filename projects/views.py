from django.shortcuts import render
from django.http import JsonResponse
from .models import Project
from django.core import serializers
import json

# Create your views here.
def projects(request):  
 
  print(f"PROJECTS")  
  all_projects =  list(Project.objects.values()) 
   
  return JsonResponse({"data": all_projects}, safe=False)