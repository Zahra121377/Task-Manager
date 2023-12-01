from django.contrib import admin, messages
from django.shortcuts import render
from django.urls import path

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "completed", "remaining_time", "priority")
    list_filter = ["completed"]
    actions = ["make_completed", "make_uncompleted"]

    @admin.action(description="Mark selected Tasks as completed")
    def make_completed(self, request, queryset):
        queryset.update(completed=True)
        message = "Tasks are marked completed successfuly."
        self.message_user(request, message, messages.SUCCESS)

    @admin.action(description="Mark selected Tasks as uncompleted")
    def make_uncompleted(self, request, queryset):
        queryset.update(completed=False)
        message = "Tasks are marked uncompleted successfuly."
        self.message_user(request, message, messages.SUCCESS)


class MyAdminSite(admin.AdminSite):
    site_header = "My Custom Admin Site"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                "task-summary/",
                self.admin_view(self.task_summary_view),
                name="task_summary",
            ),
        ]
        return custom_urls + urls

    def task_summary_view(self, request):
        tasks = Task.objects.all()
        context = {
            "title": "Task Summary",
            "tasks": tasks,
        }
        return render(request, "tasks/myadmin/task-summary.html", context)


my_admin_site = MyAdminSite(name="myadmin")
