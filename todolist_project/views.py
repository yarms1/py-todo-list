from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import generic

from todolist_project.forms import TaskCreationForm, TagsCreationForm
from todolist_project.models import Task, Tag


@login_required()
def index(request: HttpRequest) -> HttpResponse:
    all_tasks = Task.objects.all()
    completed_tasks = all_tasks.filter(is_completed=True)
    in_completed_tasks = all_tasks.filter(is_completed=False)

    context = {
        "all_tasks_count": all_tasks.count(),
        "completed_tasks_count": completed_tasks.count(),
        "in_completed_tasks_count": in_completed_tasks.count(),
    }

    return render(request, "todolist_project/index.html", context)


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskCreationForm
    success_url = reverse_lazy("todolist_project:task-list")


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    paginate_by = 5


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskCreationForm
    success_url = reverse_lazy("todolist_project:task-list")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todolist_project:task-list")


class TagCreateView(LoginRequiredMixin, generic.CreateView):
    model = Tag
    form_class = TagsCreationForm
    success_url = reverse_lazy("todolist_project:tag-list")


class TagListView(LoginRequiredMixin, generic.ListView):
    model = Tag
    paginate_by = 5


class TagDetailView(LoginRequiredMixin, generic.DetailView):
    model = Tag


class TagUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todolist_project:tag-list")


class TagDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todolist_project:tag-list")


def toggle_mark_done(request: HttpRequest, task_id: int) -> HttpResponse:
    task = get_object_or_404(Task, id=task_id)

    if task.is_completed:
        task.is_completed = False
        task.done_at = None
    else:
        task.is_completed = True
        task.done_at = timezone.now()

    task.save()

    return HttpResponseRedirect(
        request.META.get(
            "HTTP_REFERER",
            reverse_lazy(viewname="todolist_project:task-list"))
    )
