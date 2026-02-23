from django.urls import path
from . import views

urlpatterns = [
    path('accounts/register/', views.register_view, name='register'),
    path("", views.TaskBoardView.as_view(), name="task-board"),

    path("tasks/", views.TaskBoardView.as_view(), name="task-board"),

    path("projects/", views.ProjectListView.as_view(), name="project-list"),
    path("projects/create/", views.create_project, name="project-create-form"),
    path("projects/<int:project_id>/delete/", views.delete_project, name="delete-project"),

    path("teams/", views.TeamListView.as_view(), name="team-list"),
    path("teams/create/", views.create_team, name="team-create-form"),
    path("teams/<int:team_id>/delete/", views.delete_team, name="delete-team"),


    path(
        "tasks/<int:pk>/status/",
        views.update_task_status,
        name="task-status-update"
    ),
    path(
        "tasks/<int:pk>/priority/",
        views.update_task_priority,
        name="task-priority-update"
    ),
    path(
    "tasks/create/",
    views.create_task,
    name="task-create-form"
    ),
    path('tasks/<int:task_id>/delete/', views.delete_task, name='delete-task'),

]

app_name = "core"
