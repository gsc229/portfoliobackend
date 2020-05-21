from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from projects.models import Project
from django.core import serializers
from django.conf import settings
import json
# Create your views here.



def projects(request):  
 
  print(f"PROJECTS")  
  all_projects =  list(Project.objects.values()) 
  #projects = Project.objects.all()
  
  for project in all_projects:
    project['top_photo'] = settings.MEDIA_URL + project['top_photo']
  
  print(all_projects)
  # context = {
  #   'projects': all_projects
  # }

  #return render(request, 'projects/projects.html', context)
  return JsonResponse({"data": all_projects }, safe=False)


def media(request):

  req_query = request.req_query
  print(req_query)

  return HttpResponse('<h1> Looking for photos </h1>')
