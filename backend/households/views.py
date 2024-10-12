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