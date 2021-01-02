# addProject/admin.py

from django.contrib import admin
from .models import AddProject  # add this


class ProjectAdmin(admin.ModelAdmin):  # add this
    list_display = ('title', 'description', 'completed')  # add this


# Register your models here.
admin.site.register(AddProject, ProjectAdmin)  # add this
