from django.db import models
from datetime import datetime
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import ArrayField
from multiselectfield import MultiSelectField
from projects.tech_choices import TECH_CHOICES, TYPE_CHOICES
from pygments.lexers import get_all_lexers, get_lexer_by_name
# Create your models here.

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS ])


class Project(models.Model):
  title = models.CharField(max_length=200, unique=True)

  
  project_type = models.CharField(choices=TYPE_CHOICES, max_length=100, default='None')
  top_photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
  
  front_end_repo = models.CharField(max_length=500, unique=True, blank=True)
  back_end_repo = models.CharField(max_length=500, unique=True, blank=True)
  description = models.TextField(blank=True)
  roles = models.TextField(blank=True)
  responsibilities = models.TextField(blank=True)
  
  
  #technologies = MultiSelectField(choices=TECH_CHOICES)
  technologies = MultiSelectField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
  created_at = models.DateTimeField(default=datetime.now, blank=True)

  def __str__(self):
    return f"title: {self.title} created: {self.created_at}"
