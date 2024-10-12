import django_filters
from .models import Task

class TaskFilter(django_filters.FilterSet):
    assigned_to_username = django_filters.CharFilter(
        field_name='assigned_to__username',
        lookup_expr='icontains'
    )

    class Meta:
        model = Task
        fields = [
            'title', 'due_date', 'status', 'assigned_to_username'
        ]