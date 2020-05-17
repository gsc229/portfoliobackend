from django.shortcuts import render
from django.http import JsonResponse
from projects.models import Project
from django.core import serializers
import json

# Create your views here.
def projects(request):  
 
  print(f"PROJECTS")  
  all_projects =  list(Project.objects.values()) 
  
  print(Project.objects.all()[0].top_photo.url)

  return JsonResponse({"data": all_projects }, safe=False)