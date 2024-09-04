from django.contrib import admin

from .models import UserProfile, TaskCompletion

admin.site.register(UserProfile)
admin.site.register(TaskCompletion)

