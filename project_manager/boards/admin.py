from django.contrib import admin
from .models import Project  # Импортируем Project вместо Board

admin.site.register(Project)