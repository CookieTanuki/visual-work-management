from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Position, Worker, Tag, TaskType, Team, Project, Task

@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position",)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("position",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Info", {"fields": ("position",)}),
    )

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "status",
        "priority",
        "task_type",
        "project",
        "deadline",
        "created_by"
    )

    list_select_related = ("task_type", "project", "created_by")
    # Боковая панель фильтрации
    list_filter = ("status", "priority", "task_type", "project", "tags")
    # Поиск по названию задачи и описанию
    search_fields = ("name", "description")
    # Позволяет выбирать много исполнителей и тегов
    filter_horizontal = ("assignees", "tags")
    # Автоматическая дата создания
    readonly_fields = ("created_at", "updated_at")
    # Новые задачи начинаются сверху
    ordering = ("-created_at",)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "team", "created_at")
    list_filter = ("team",)
    search_fields = ("name",)

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name",)
    filter_horizontal = ("members",)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "color")

admin.site.register(Position)
admin.site.register(TaskType)