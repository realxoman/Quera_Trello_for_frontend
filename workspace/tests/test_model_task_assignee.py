from django.test import TestCase
from workspace.models import Workspace, Project, Board, Task, TaskAssignee
from django.contrib.auth import get_user_model


class TaskAssigneeTest(TestCase):

    def setUp(self):
        # create a creator test user
        self.creator = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )

        # create a member test user
        self.member = get_user_model().objects.create_user(
            username='testmember',
            password='memberpassword'
        )

        self.workspace = Workspace(
            name='testname',
            creator=self.creator
        )

        self.project = Project(
            workspace=self.workspace
        )

        self.board = Board(
            project=self.project,
            name='testname'
        )

        self.task = Task(
            board=self.board,
            name='testname'
        )

        self.taskassignee = TaskAssignee(
            Task=self.task,
            user=self.member
        )

    def test_model_str(self):
        self.assertEqual(str(self.taskassignee), 'testname')
