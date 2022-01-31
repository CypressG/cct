# from typing_extensions import Required
from rest_framework import serializers
from api.models import Group, Registry, Meeting
from api.data_settings import (
    GROUP_NAME_LENGTH,
    MEETING_ROOM_LENGTH,
    MEETING_SUBJECT_LENGTH,
)
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("email", "first_name", "last_name")


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("id", "name")


class RegistrySerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.email")

    class Meta:
        model = Registry
        fields = ("id", "user", "group", "is_leader")
        read_only_fields = ("is_leader",)


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
