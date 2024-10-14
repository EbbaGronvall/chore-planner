from rest_framework import serializers
from .models import Profile
from households.models import Household
from households.serializers import HouseholdSerializer


class ProfileSerializer(serializers.ModelSerializer):
    member = serializers.ReadOnlyField(source='member.username')
    is_member = serializers.SerializerMethodField()
    household = serializers.PrimaryKeyRelatedField(queryset=Household.objects.all())

    def get_is_member(self, obj):
        request = self.context['request']
        return request.user == obj.member

    class Meta:
        model = Profile
        fields = [
            'id', 'member', 'role', 'household',
            'is_member',
        ]