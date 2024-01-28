from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ["creation_time", "completion_time"]
    fields = ["name", "description", "status", "creation_time", "completion_time"]


admin.site.register(Task, TaskAdmin)
