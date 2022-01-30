from django.test import TestCase
from .models import User

# Create your tests here.
class UserTestCase(TestCase):
    def setUp(self):
        user = User(username="test", email="test@test.com")
        user.is_staff = True
        user.is_superuser = True
        user.set_password("test")
        user.save()
        print(user.id)

    def test_user_check(self):
        user_count = User.objects.all().count()
        expected_count = 1
        print(f"Expected user count: {expected_count} | Got: {user_count}")
        self.assertEqual(user_count, expected_count)
