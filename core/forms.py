from django import forms
from django.contrib.auth.forms import UserCreationForm
from core.models import Task, Worker, Project

class WorkerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name", "email", "position",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none'
            else:
                field.widget.attrs['class'] = 'w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none'


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "name",
            "description",
            "task_type",
            "project",
            "assignees",
            "priority",
            "deadline",
        ]
        widgets = {
            "deadline": forms.DateInput(
                attrs={"type": "date"}
            ),
            "assignees": forms.CheckboxSelectMultiple(attrs={
                'class': 'grid grid-cols-2 gap-2 mt-1'}
            ),
            "tags": forms.SelectMultiple(
                attrs={"class": "w-full"}
            ),
            "description": forms.Textarea(attrs={'rows': 3, 'class': 'w-full border rounded-lg px-3 py-2'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'w-full border rounded-lg px-3 py-2'})

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["name", "team"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'w-full border rounded-lg px-3 py-2'})
