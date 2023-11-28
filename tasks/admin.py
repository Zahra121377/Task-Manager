from django.contrib import admin
from django.contrib.auth.models import Group, User

from .models import Task

# Register your models here.
admin.site.unregister(Group)
admin.site.unregister(User)


@admin.action(description="Mark selected Tasks as completed")
def make_completed(modeladmin, request, queryset):
    queryset.update(completed=True)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "completed", "remaining_time", "priority")
    list_filter = ["completed"]
    actions = [make_completed]
