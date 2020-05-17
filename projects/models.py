from django.db import models
from datetime import datetime
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import ArrayField
from multiselectfield import MultiSelectField
# Create your models here.
class Project(models.Model):
  title = models.CharField(max_length=200, unique=True)

  TYPE_CHOICES = (
    ('Course Project', 'Course Project'),
    ('Major Project', 'Major Project'),    
    ('Week Project', 'Week Project'),
    ('Personal Day Project', 'Personal Day Project'),
    ('None', 'None')
  )
  project_type = models.CharField(choices=TYPE_CHOICES, max_length=100, default='None')
  top_photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
  front_end_repo = models.CharField(max_length=500, unique=True, blank=True)
  back_end_repo = models.CharField(max_length=500, unique=True, blank=True)
  description = models.TextField(blank=True)
  roles = models.TextField(blank=True)
  responsibilities = models.TextField(blank=True)
  
  TECH_CHOICES = (
    ('Python', 'Python'),     
    ('Django','Django'),      
    ('React with hooks','React with hooks'),     
    ('React with classes','React with classes'),       
    ('React Router','React Router'),      
    ('JavaScript','JavaScript'),   
    ('Node','Node'),      
    ('Express','Express'),    
    ('MongoDB','MongoDB'),       
    ('Mongoose','Mongoose'),      
    ('Angular','Angular'),       
    ('Postgres','Postgres'),       
    ('Bootstrap','Bootstrap'),     
    ('Heroku','Heroku'),
    ('Amazon Web Services','Amazon Web Services'),
    ('Digital Ocean','Digital Ocean'),    
    ('Jinja','Jinja'),    
    ('Styled Components','Styled Components'),
    ('CSS 3','CSS 3'),    
    ('Material UI','Material UI'),        
    ('Materialize','Materialize'),
    ('Sass','Sass'),
    ('Less','Less'),    
    ('HTML 5','HTML 5'),    
    ('Axios','Axios'),
    ('None','None')
  )
    
  technologies = MultiSelectField(choices=TECH_CHOICES)
  created_at = models.DateTimeField(default=datetime.now, blank=True)

  def __str__(self):
    return f"title: {self.title} created: {self.created_at}"







""" 
class Technology(models.TextChoices):
    PYTHON = 'PY', _('Python')
    DJANGO = 'DJ', _('Django')
    REACTHOOKS = 'RH', _('React with hooks')
    REACTCLASS = 'RC', _('React with classes')
    REACTROUTER = 'RR', _('React Router')
    JAVASCRIPT = 'JS', _('JavaScript')
    NODE = 'NO', _('Node')
    EXPRESS = 'EX', _('Express')
    MONGO = 'MG', _('MongoDB')
    MONGOOSE = 'MS', _('Mongoose')  
    ANGULAR = 'AG', _('Angular')  
    POSTGRES = 'PG', _('Postgres')
    BOOTSTAP = 'BS', _('Bootstrap')
    HEROKU = 'HE', _('Heroku')
    AWS = 'AW', _('Amazon Web Services')
    DO = 'DO', _('Digital Ocean')
    JINJA = 'JN', _('Jinja')
    SC = 'SC', _('Styled Components')
    CSS3 = 'C3', _('CSS 3')
    MATERIALUI = 'MU', _('Material UI')
    MATERIALIZE = 'MZ', _('Materialize')
    SASS = 'SS', _('Sass')
    LESS = 'LS', _('Less')
    HTML5 = 'H5', _('HTML 5')
    AXIOS = 'AX', _('Axios')
    NONE = 'NA', _('None')
  technologies = ArrayField(
    models.CharField(
      max_length=2,
      choices=Technology.choices,
      default=Technology.NONE
    ),     
    blank=True)


"""