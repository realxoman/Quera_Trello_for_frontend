from django.test import TestCase
from workspace.models import Workspace, Project
from django.contrib.auth import get_user_model


class ProjectTest(TestCase):
    def setUp(self):
        # create a test user
        self.user = get_user_model().objects.create_user(
            username="testuser", password="testpassword"
        )

        self.workspace = Workspace(name="testname", creator=self.user)

        self.project = Project(workspace=self.workspace, name=1)

    def test_model_name(self):
        self.assertEqual(self.project.name, 1)

    def test_model_str(self):
        self.assertEqual(str(self.project), "1")
