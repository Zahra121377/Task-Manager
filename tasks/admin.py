from django.contrib import admin
from .models import Task
from django.contrib.auth.models import Group, User

# Register your models here.
admin.site.register(Task)
admin.site.unregister(Group)
admin.site.unregister(User)
