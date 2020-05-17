from django.db import models
from datetime import datetime
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class Project(models.Model):
  title = models.CharField(max_length=200, unique=True)
  description = models.TextField(blank=True)
  roles = models.TextField(blank=True)
  responsibilities = models.TextField(blank=True)

  class Technology(models.TextChoices):
    PYTHON = 'PY', _('Python')
    DJANGO = 'DJ', _('Django')
    REACT = 'RE', _('React')
    JAVASCRIPT = 'JS', _('JavaScript')
    NODE = 'NO', _('Node')
    EXPRESS = 'EX', _('Express')
    MONGO = 'MG', _('MongoDB')
    MONGOOSE = 'MS', _('Mongoose')    
    POSTGRES = 'PG', _('Postgres')
    BOOTSTAP = 'BS', _('Bootstrap')
    HEROKU = 'HE', _('Heroku')
    AWS = 'AW', _('Amazon Web Services')
    DO = 'DO', _('Digital Ocean')
    JINJA = 'JN', _('Jinja')
    NONE = 'NA', _('None')
  technologies = ArrayField(
    models.CharField(
      max_length=2,
      choices=Technology.choices,
      default=Technology.NONE
    ),     
    blank=True)
  created_at = models.DateTimeField(default=datetime.now, blank=True)
  front_end_repo = models.CharField(max_length=500, unique=True)
  back_end_repo = models.CharField(max_length=500, unique=True)



  def __str__(self):
    return f"title: {self.title} created: {self.created_at}"


    """ 
    models.CharField(
    max_length=2,
    choices=Technology.choices,
    default=Technology.NONE
    )
    
    
    """