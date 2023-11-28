from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.contrib import messages
from .models import Task

# Register your models here.
admin.site.unregister(Group)
admin.site.unregister(User)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "completed", "remaining_time", "priority")
    list_filter = ["completed"]
    actions = ["make_completed", "make_uncompleted"]
    

    @admin.action(description="Mark selected Tasks as completed")
    def make_completed(self, request, queryset):
        updated = queryset.update(completed=True)
        message = "Tasks are marked completed successfuly."
        self.message_user(request, message, messages.SUCCESS) 
        
    @admin.action(description="Mark selected Tasks as uncompleted")
    def make_uncompleted(self, request, queryset):
        updated = queryset.update(completed=False)
        message = "Tasks are marked uncompleted successfuly."
        self.message_user(request, message, messages.SUCCESS)