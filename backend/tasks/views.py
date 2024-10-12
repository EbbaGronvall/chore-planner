from rest_framework import generics, filters
from .models import Task
from .serializers import TaskSerializer
from .filters import TaskFilter
from chore_api.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

class TaskList(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_class = TaskFilter
    filterset_fields = [
        'title', 'due_date', 'status', 'assigned_to__username'
    ]
    search_fields = ['member']
    ordering_fields = [
        'title', 'due_date', 'status', 'assigned_to__username'
    ]

    def get_queryset(self):
        user_profile = self.request.user.profile
        return Task.objects.filter(assigned_to__household=user_profile.household)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context