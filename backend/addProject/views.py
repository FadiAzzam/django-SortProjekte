# AddProject/views.py

from django.shortcuts import render
from rest_framework import viewsets          # add this
from .serializers import ProjektSerializer      # add this
from .models import AddProject                     # add this


class ProjectView(viewsets.ModelViewSet):       # add this
    serializer_class = ProjektSerializer          # add this
    queryset = AddProject.objects.all()
