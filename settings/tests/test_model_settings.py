from django.test import TestCase
from settings.models.model_settings import Settings
from django.contrib.auth import get_user_model


class SettingsTest(TestCase):

    def setUp(self):
        # create a test user
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )

        self.settings = Settings(
            user=self.user,
            theme=1
        )

    def test_model_theme(self):
        self.assertEqual(self.settings.theme, 1)

    def test_model_str(self):
        self.assertEqual(str(self.settings), '1')
