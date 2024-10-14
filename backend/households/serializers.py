from rest_framework import serializers
from .models import Household


class HouseholdSerializer(serializers.ModelSerializer):
    members = serializers.SerializerMethodField()

    def get_members(self, obj):
        return [profile.member.username for profile in obj.members.all()]

    class Meta:
        model = Household
        fields = [
            'id', 'name', 'slug', 'members'
        ]