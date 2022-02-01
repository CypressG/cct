# from typing_extensions import Required
from rest_framework import serializers
from api.models import Group, Registry, Meeting, Room
from django.contrib.auth import get_user_model
import logging

logger = logging.getLogger(__name__)


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
    class Meta:
        model = Registry
        fields = ("id", "user", "group", "is_leader")
        read_only_fields = ("is_leader",)

    def get_user(self, profile):
        return profile.user.email

    def to_representation(self, instance):
        logger.info("Started performing representation")
        representation = super().to_representation(instance)
        representation["group"] = GroupSerializer(instance.group).data
        representation["user"] = UserSerializer(instance.user).data
        logger.info("Finished performing representation")
        logger.info(representation)
        return representation


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

    def to_representation(self, instance):
        logger.info("Started performing representation")
        representation = super().to_representation(instance)
        representation["group"] = GroupSerializer(instance.group).data
        representation["room"] = RoomSerializer(instance.room).data
        logger.info("Finished performing representation")
        logger.info(representation)
        return representation

    def validate(self, data):
        """
        Check that start is before finish.
        """

        if data["start_time"] > data["end_time"]:
            raise serializers.ValidationError("finish must occur after start")
        return data
