from django.contrib.auth import get_user_model
from django.db import models

from project.models import Project

User = get_user_model()


class Task(models.Model):
    class StatusChoices(models.TextChoices):
        TODO = 'todo', 'todo'
        IN_PROGRESS = 'in_progress', 'in_progress'
        DONE = 'done', 'done'

    title = models.CharField(max_length=255, unique=True, )
    description = models.TextField(null=True, blank=True, )
    status = models.CharField(max_length=255, choices=StatusChoices.choices, default=StatusChoices.TODO, )
    user = models.ForeignKey(to=User, on_delete=models.PROTECT, )
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE, )

    def __str__(self):
        return f"{self.project.title} - {self.title}"
