from django.db import models
from django.core.exceptions import ValidationError
from profiles.models import Profile
from django.utils import timezone

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
    member = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='tasks')

    def clean(self):
        if self.due_date < timezone.now().date():
            raise ValidationError('Due date can not be in the past.')

    def save(self, *args, **kwargs):
        self.clean()
        super(Task, self).save(*args, **kwargs)
        
    class Meta:
        ordering = ['-due_date']
    
    def __str__(self):
        return self.title

