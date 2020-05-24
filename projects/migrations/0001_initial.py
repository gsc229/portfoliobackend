# Generated by Django 3.0.6 on 2020-05-23 06:54

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('project_type', models.CharField(choices=[('Course Project', 'Course Project'), ('Team Projct', 'Team Project'), ('Major Project', 'Major Project'), ('Week Project', 'Week Project'), ('Personal Day Project', 'Personal Day Project'), ('None', 'None')], default='None', max_length=100)),
                ('top_photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('front_end_repo', models.CharField(blank=True, max_length=500, unique=True)),
                ('back_end_repo', models.CharField(blank=True, max_length=500, unique=True)),
                ('website', models.CharField(blank=True, max_length=500, unique=True)),
                ('description', models.TextField(blank=True)),
                ('roles', models.TextField(blank=True)),
                ('responsibilities', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('technologies', multiselectfield.db.fields.MultiSelectField(choices=[('Python', 'Python'), ('Django', 'Django'), ('React with hooks', 'React with hooks'), ('React with classes', 'React with classes'), ('React Router', 'React Router'), ('JavaScript', 'JavaScript'), ('Node', 'Node'), ('Express', 'Express'), ('MongoDB', 'MongoDB'), ('Mongoose', 'Mongoose'), ('Angular', 'Angular'), ('Postgres', 'Postgres'), ('Bootstrap', 'Bootstrap'), ('Heroku', 'Heroku'), ('Amazon Web Services', 'Amazon Web Services'), ('Digital Ocean', 'Digital Ocean'), ('Jinja', 'Jinja'), ('Styled Components', 'Styled Components'), ('CSS 3', 'CSS 3'), ('Material UI', 'Material UI'), ('Materialize', 'Materialize'), ('Sass', 'Sass'), ('Less', 'Less'), ('HTML 5', 'HTML 5'), ('Axios', 'Axios'), ('None', 'None')], default='None', max_length=253)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
