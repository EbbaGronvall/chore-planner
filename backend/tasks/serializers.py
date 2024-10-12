from rest_framework import serializers
from django.utils import timezone
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'created_at',
            'due_date', 'status', 'member',
        ]
    def validate_due_date(self, value):
        if value < timezone.now().date():
            raise serializers.ValidationError('Due date can not be in the past.')
        return value