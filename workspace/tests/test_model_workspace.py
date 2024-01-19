from django.test import TestCase
from workspace.models import Workspace
from django.contrib.auth import get_user_model


class WorkspaceTest(TestCase):
    def setUp(self):
        # create a test user
        self.user = get_user_model().objects.create_user(
            username="testuser", password="testpassword"
        )

        self.workspace = Workspace(
            name="testname", creator=self.user, thumbnail_alt="testalt"
        )

    def test_model_name(self):
        self.assertEqual(self.workspace.name, "testname")

    def test_model_thumbnail_alt(self):
        self.assertEqual(self.workspace.thumbnail_alt, "testalt")

    def test_model_str(self):
        self.assertEqual(str(self.workspace), "testname")
