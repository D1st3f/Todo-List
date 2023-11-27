from django.contrib import admin
from .models import Tag, Task


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('content', 'datetime_field', 'deadline', 'task_done')
    list_filter = ('task_done', 'tags')
    search_fields = ('content', 'tags__name')
    date_hierarchy = 'datetime_field'
