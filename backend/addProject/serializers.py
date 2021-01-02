# AddProject/serializers.py

from rest_framework import serializers
from .models import AddProject


class ProjektSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddProject
        fields = ('id', 'title', 'description', 'completed')
