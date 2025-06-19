from rest_framework import serializers
from .models import Bug

class BugSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    project = serializers.CharField(source='project.name', read_only=True)

    class Meta:
        model = Bug
        fields = ['id', 'description', 'username', 'project']
