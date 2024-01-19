from django.test import TestCase
from account.models import CustomUser


class CustomUserTest(TestCase):
    def setUp(self):
        # create a test user
        self.username = CustomUser(username="testuser", is_superuser=0, is_staff=1)

    def test_model_user(self):
        self.assertEqual(self.username.username, "testuser")

    def test_model_is_superuser(self):
        self.assertEqual(self.username.is_superuser, 0)

    def test_model_is_staff(self):
        self.assertEqual(self.username.is_staff, 1)

    def test_model_str(self):
        self.assertEqual(str(self.username), "testuser")
