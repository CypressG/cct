from django.db import models
from django.conf import settings
from api.data_settings import (
    GROUP_NAME_LENGTH,
    MEETING_ROOM_LENGTH,
    MEETING_SUBJECT_LENGTH,
)


# A name of a group who's having a meeting.
class Group(models.Model):
    name = models.CharField(max_length=GROUP_NAME_LENGTH)

    def __str__(self):
        return f"{self.id} | {self.name}"


# Register which shows who belong to which group
# a peerson can be in multiple groups
class Registry(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    is_leader = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id} | {self.user} "


# Meeting detailed information
class Meeting(models.Model):
    subject = models.CharField(max_length=MEETING_SUBJECT_LENGTH)
    room = models.CharField(max_length=MEETING_ROOM_LENGTH)
    start_time = models.DateTimeField(blank=True)
    end_time = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.subject} | {self.room}"
