from django.test import TestCase
from .models import User
from .mock_data import USER_MOCK_DATA

# Create your tests here.
class UserTestCase(TestCase):
    def setUp(self):
        # Setting up users from mock data global variable
        for x in range(len(USER_MOCK_DATA)):
            user = User(
                first_name=USER_MOCK_DATA[x]["first_name"],
                last_name=USER_MOCK_DATA[x]["last_name"],
                email=USER_MOCK_DATA[x]["email"],
            )
            # Assigning privelleges and permissions to the user
            user.is_superuser = True
            user.set_password(USER_MOCK_DATA[x]["password"])
            user.save()
            print(user.id)

    # Checking if the user count is the same as a given data
    def test_user_check(self):
        user_count = User.objects.all().count()
        expected_count = len(USER_MOCK_DATA)
        print(f"Expected user count: {expected_count} | Got: {user_count}")
        self.assertEqual(user_count, expected_count)
