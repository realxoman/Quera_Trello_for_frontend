from django.test import TestCase
from workspace.models import Workspace, Project, ProjectMember
from django.contrib.auth import get_user_model


class ProjectMemberTest(TestCase):

    def setUp(self):
        # create a test creator user
        self.creator = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )

        # create a test member user
        self.member = get_user_model().objects.create_user(
            username='testmember',
            password='memberpassword'
        )

        self.workspace = Workspace(
            name='testname',
            creator=self.creator
        )

        self.project = Project(
            workspace=self.workspace,
            name=1
        )

        self.project_member = ProjectMember(
            project=self.project,
            user=self.member
        )

    def test_model_str(self):
        self.assertEqual(str(self.project_member), '1')
