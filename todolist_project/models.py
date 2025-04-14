from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    done_at = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    def __str__(self):
        return (f"Task: {self.content[:20]}... |"
                f" Created at: {self.created_at} |"
                f" Deadline: {self.deadline} |"
                f" Completed: {self.is_completed}")

    class Meta:
        ordering = ["done_at", "-created_at"]
