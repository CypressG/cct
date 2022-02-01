from django.test import TestCase
from api.models import Group, Meeting, Room
from api.mock_data import (
    GROUP_MOCK_DATA,
    MEETING_MOCK_DATA,
    USER_MOCK_DATA,
    ROOM_MOCK_DATA,
)
from django.contrib.auth import get_user_model


# prep database
def create_group_mock_data():
    for x in range(len(GROUP_MOCK_DATA)):
        group = Group(
            name=GROUP_MOCK_DATA[x]["name"],
        )
        group.save()
    print(get_user_model()._meta.get_fields())


def create_user_mock_data():
    User = get_user_model()
    for x in range(len(GROUP_MOCK_DATA)):
        user = User(
            email=USER_MOCK_DATA[x]["email"],
            first_name=USER_MOCK_DATA[x]["first_name"],
            last_name=USER_MOCK_DATA[x]["last_name"],
        )
        print(user)
        user.set_password(USER_MOCK_DATA[x]["password"])
        user.save()


def create_room_mock_data():
    for x in range(len(ROOM_MOCK_DATA)):
        room = Room(
            name=ROOM_MOCK_DATA[x]["name"],
        )
        room.save()
        print(room)


def create_meeting_mock_data():
    for x in range(len(MEETING_MOCK_DATA)):
        meeting = Meeting(
            subject=MEETING_MOCK_DATA[x]["subject"],
            room=Room.objects.get(pk=MEETING_MOCK_DATA[x]["room"]),
            start_time=MEETING_MOCK_DATA[x]["start_time"],
            end_time=MEETING_MOCK_DATA[x]["end_time"],
            group=Group.objects.get(pk=MEETING_MOCK_DATA[x]["group"]),
        )
        meeting.save()
        print(Meeting.objects.all())


# Create your tests here.
class GroupTestCase(TestCase):
    def setUp(self):
        create_group_mock_data()
        # Setting up users from mock data global variable

    def test_group_check(self):
        group_count = Group.objects.all().count()
        expected_count = len(GROUP_MOCK_DATA)
        print(f"Expected group count: {expected_count} | Got: {group_count}")
        self.assertEqual(group_count, expected_count)


class MeetingTestCase(TestCase):
    def setUp(self):
        create_group_mock_data()
        create_room_mock_data()
        create_meeting_mock_data()

    def test_meeting_check(self):
        meeting_count = Meeting.objects.all().count()
        expected_count = len(MEETING_MOCK_DATA)
        print(f"Expected user count: {expected_count} | Got: {meeting_count}")
        self.assertEqual(meeting_count, expected_count)


class RoomTestCase(TestCase):
    def setUp(self):
        create_room_mock_data()

    def test_room_check(self):
        room_count = Room.objects.all().count()
        expected_count = len(ROOM_MOCK_DATA)
        print(f"Expected user count: {expected_count} | Got: {room_count}")
        self.assertEqual(room_count, expected_count)
