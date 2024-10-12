from rest_framework import serializers
from django.utils import timezone
from .models import Task
from profiles.models import Profile

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

    def validate_member(self, value):
        request = self.context.get('request')
        user_profile = request.user.profile
        if user_profile.role != 'Parent':
            raise serializers.ValidationError('Only parents can assign tasks.')
        
        if user_profile.household != value.household:
            raise serializers.ValidationError('You can only assign tasks to members of the same household as you!')
        return value