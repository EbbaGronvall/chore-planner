from rest_framework import generics, filters
from .models import Task
from .serializers import TaskSerializer
from chore_api.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

class TaskList(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_fields = [
        'title', 'due_date', 'status', 'member'
    ]
    search_fields = ['member']
    ordering_fields = [
        'title', 'due_date', 'status', 'member'
    ]

    def get_queryset(self):
        user_profile = self.request.user.profile
        return Task.objects.filter(member__household=user_profile.household)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context