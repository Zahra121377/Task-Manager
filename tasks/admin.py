from django.contrib import admin
from django.contrib.auth.models import Group, User

from .models import Task

# Register your models here.
admin.site.register(Task)
admin.site.unregister(Group)
admin.site.unregister(User)
