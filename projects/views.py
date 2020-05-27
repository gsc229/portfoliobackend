from rest_framework import generics, renderers, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from projects.models import Project
from django.contrib.auth.models import User
from projects.serializers import ProjectSerializer
#from projects.serializers


@api_view(['GET'])
def api_root(request, format=None):
  
  return Response({
    'projects': reverse('project-list', request=request, format=format)
    
  })

""" GET all, POST """
class ProjectList(generics.ListCreateAPIView):
  queryset = Project.objects.all()
  serializer_class = ProjectSerializer
  permission_classes  = [permissions.IsAuthenticatedOrReadOnly]
  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)

""" GET single, PUT, DELTE """
class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Project.objects.all()
  serializer_class = ProjectSerializer
  permission_classes  = [permissions.IsAuthenticatedOrReadOnly]



""" 
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

  return HttpResponse('<h1> Looking for photos </h1>') """
