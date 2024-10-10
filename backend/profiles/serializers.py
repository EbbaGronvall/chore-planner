from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    member = serializers.ReadOnlyField(source='member.username')

    class Meta:
        model = Profile
        fields = [
            'id', 'member', 'role', 'household'
        ]