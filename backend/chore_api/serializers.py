from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    member_id = serializers.ReadOnlyField(source='member.id')
    member_name = serializers.ReadOnlyField(source='member.username')

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'member_id', 'member_name'
        )