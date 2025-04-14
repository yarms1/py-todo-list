from django import forms
from django.forms import DateInput
from todolist_project.models import Task, Tag


class TaskCreationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "content",
            "deadline",
            "tags",
        ]
        widgets = {
            "deadline": DateInput(attrs={"type": "date"}),
        }


class TagsCreationForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
