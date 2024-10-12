from django.db import models
from profiles.models import Profile

# A model for the tasks

class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    title = models.CharField(max_length=30)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    assigned_to = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='tasks')

    class Meta:
        ordering = ['-due_date']
    
    def __str__(self):
        return self.title

