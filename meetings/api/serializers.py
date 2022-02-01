# from typing_extensions import Required
from rest_framework import serializers
from api.models import Group, Registry, Meeting, Room
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("email", "first_name", "last_name")
        read_only_fields = ("email", "first_name", "last_name")


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("id", "name")


class RegistrySerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field="email", many=True, read_only=True
    )

    class Meta:
        model = Registry
        fields = ("id", "user", "group", "is_leader")
        read_only_fields = ("is_leader",)

    def get_user(self, profile):
        return profile.user.email


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ("id", "name")


class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = (
            "id",
            "subject",
            "room",
            "start_time",
            "end_time",
            "created",
            "group",
        )
        depth = 1
