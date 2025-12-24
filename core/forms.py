from django import forms
from core.models import Task


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
