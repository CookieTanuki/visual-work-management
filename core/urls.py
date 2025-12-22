from django.urls import path
from . import views

urlpatterns = [
    path("", views.TaskBoardView.as_view(), name="task-board"),

    path("tasks/", views.TaskBoardView.as_view(), name="task-board"),

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
]

app_name = "core"
