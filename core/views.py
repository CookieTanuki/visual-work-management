from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required

from core.forms import TaskForm
from core.models import Task, Project


class TaskBoardView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "tasks/board.html"
    context_object_name = "tasks"

    def get_queryset(self):
        queryset = (Task
                    .objects
                    .select_related("task_type", "project", "created_by")
                    .prefetch_related("assignees", "tags"))

        if self.request.GET.get("filter") == "my":
            return queryset.filter(assignees=self.request.user)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tasks = context["tasks"]

        context["board"] = [
            {
                "value": value,
                "label": label,
                "tasks": tasks.filter(status=value),
            }
            for value, label in Task.Status.choices
        ]

        return context


@login_required
@require_http_methods(["POST"])
def update_task_status(request, pk):
    task = get_object_or_404(Task.objects.prefetch_related("assignees"), pk=pk)
    is_author = task.created_by == request.user
    is_assignee = task.assignees.filter(pk=request.user.pk).exists()

    if not (is_author or is_assignee):
        raise PermissionDenied("You cannot change the status of someone else's task if you are not the assignee.")

    new_status = request.POST.get("status")
    if new_status in Task.Status.values:
        task.status = new_status
        task.save(update_fields=["status"])

    row_html = render_to_string("tasks/partials/task_row.html", {"task": task}, request=request)

    target_id = f"tasks-{task.status.upper()}"

    obb_row_html = row_html.replace(
        '<tr ',
        f'<tr hx-swap-oob="afterbegin:#{target_id}" '
    )

    return HttpResponse(obb_row_html)


@login_required
@require_http_methods(["POST"])
def update_task_priority(request, pk):
    task = get_object_or_404(Task.objects.select_related("created_by"), pk=pk)
    if task.created_by != request.user:
        raise PermissionDenied("Only the task owner/creator has permission to modify its priority.")

    new_priority = request.POST.get("priority")
    if new_priority in Task.Priority.values:
        task.priority = new_priority
        task.save(update_fields=["priority"])

    return render(request, "tasks/partials/task_priority_badge.html", {"task": task})


@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user
            task.status = task.Status.TODO
            task.save()
            form.save_m2m()

            return render(
                request,
                "tasks/partials/task_row.html",
                {"task": task}
            )
    else:
        form = TaskForm()

    return render(
        request,
        "tasks/partials/task_form_modal.html",
        {"form": form}
    )

@login_required
@require_http_methods(["DELETE"])
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, created_by=request.user)
    task.delete()
    return HttpResponse("")