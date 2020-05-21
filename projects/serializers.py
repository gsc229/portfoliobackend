from rest_framework import serializers
from projects.models import Project
from django.contrib.auth.models import User


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = [
                'title', 
                'project_type', 
                'top_photo', 
                'front_end_repo', 
                'back_end_repo', 
                'description', 
                'roles', 
                'responsibilities',
                'technologies', 
                'created_at'
                ]
    
    def create(self, validated_data):
        return Project.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.project_type = validated_data.get('project_type', instance.project_type)
        instance.top_photo = validated_data.get('top_photo', instance.top_photo)
        instance.front_end_repo = validated_data.get('front_end_repo', instance.front_end_repo)
        instance.back_end_repo = validated_data.get('back_end_repo', instance.back_end_repo)
        instance.description = validated_data.get('description', instance.description)
        instance.roles = validated_data.get('roles', instance.roles) 
        instance.responsibilities = validated_data.get('responsibilities', instance.responsibilities)        
        instance.technologies = validated_data.get('technologies', instance.technologies)
        instance.created_at = validated_data.get('created_at', instance.created_at)
            
