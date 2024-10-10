from rest_framework import serializers
from .models import Household
from profiles.serializers import ProfileSerializer

class HouseholdSerializer(serializers.ModelSerializer):
    members = ProfileSerializer(many=True, read_only=True)

    class Meta:
        model = Household
        fields = [
            'id', 'name', 'slug', 'members'
        ]