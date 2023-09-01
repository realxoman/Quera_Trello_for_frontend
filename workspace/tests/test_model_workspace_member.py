from django.test import TestCase
from workspace.models import Workspace, WorkspaceMember
from django.contrib.auth import get_user_model


class WorkspaceMemberTest(TestCase):

    def setUp(self):
        # creates a test creator user
        self.creator = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )

        # creates a test member user
        self.member = get_user_model().objects.create_user(
            username='testmember',
            password='memberpass'
        )

        self.workspace = Workspace(
            name='testname',
            creator=self.creator
        )
        self.workspace_member = WorkspaceMember(
            workspace=self.workspace,
            user=self.member,
            role='testrole'
        )

    def test_model_role(self):
        self.assertEqual(self.workspace_member.role, 'testrole')

    def test_model_str(self):
        self.assertEqual(str(self.workspace_member), 'testname')
