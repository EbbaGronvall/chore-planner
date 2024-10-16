from django.shortcuts import get_object_or_404
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Household
from .serializers import HouseholdSerializer
from chore_api.permissions import IsOwnerOrReadOnly

class HouseholdList(generics.ListAPIView):
    serializer_class = HouseholdSerializer
    queryset = Household.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter
    ]
    filterset_fields = [
        'name', 'members__member__username'
    ]
    search_fields = [
        'name', 'members__member__username'
    ]

class HouseholdDetail(generics.RetrieveUpdateAPIView):
    serializer_class = HouseholdSerializer
    queryset = Household.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [
        'members__member__username', 'members__member__role'
    ]

    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Household, slug=slug)