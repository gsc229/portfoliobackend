# Generated by Django 3.0.6 on 2020-05-24 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20200524_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='back_end_repo',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='project',
            name='front_end_repo',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='project',
            name='website',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
