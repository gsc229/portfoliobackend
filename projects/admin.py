from django.contrib import admin
from .models import Project
# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'description')
  list_display_links = ('id', 'title')
  search_fields = ('title', 'description')
  list_per_page = 25
admin.site.register(Project, ProjectAdmin)