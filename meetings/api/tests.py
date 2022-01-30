from django.test import TestCase
from api.models import Group
from api.mock_data import GROUP_MOCK_DATA


# Create your tests here.
class GroupTestCase(TestCase):
    def setUp(self):
        # Setting up users from mock data global variable
        for x in range(len(GROUP_MOCK_DATA)):
            group = Group(
                name=GROUP_MOCK_DATA[x]["name"],
            )
            group.save()
            print(group.id)

    def test_group_check(self):
        group_count = Group.objects.all().count()
        expected_count = len(GROUP_MOCK_DATA)
        print(f"Expected user count: {expected_count} | Got: {group_count}")
        self.assertEqual(group_count, expected_count)
