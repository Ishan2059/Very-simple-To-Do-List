from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)  # Stores the task's name.
    completed = models.BooleanField(default=False)  # Tracks if the task is done.
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for task creation.
    
    def __str__(self):
        return self.title