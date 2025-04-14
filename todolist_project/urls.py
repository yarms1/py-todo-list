from django.urls import path
from todolist_project.views import (
    index,
    TaskListView,
    TagListView,
    TaskDetailView,
    TaskDeleteView,
    TaskUpdateView,
    TaskCreateView,
    TagCreateView,
    TagDeleteView,
    TagUpdateView,
    toggle_mark_done,
    TagDetailView
)

app_name = "todolist_project"

urlpatterns = [
    path("", index, name="index"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("toggle_mark_done/<int:task_id>/", toggle_mark_done, name="toggle-mark-done"),
    path("tags/<int:pk>/", TagDetailView.as_view(), name="tags-detail"),
]
