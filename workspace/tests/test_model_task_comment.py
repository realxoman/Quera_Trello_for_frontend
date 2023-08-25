from django.test import TestCase
from workspace.models import Workspace, Project, Board, Task, TaskComment
from django.contrib.auth import get_user_model


class TaskCommentTest(TestCase):

    def setUp(self):
        # create a test user
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )

        self.workspace = Workspace(
            name='testname',
            creator=self.user
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

        self.comment = TaskComment(
            task=self.task,
            author=1,
            text='testtext'
        )

    def test_model_author(self):
        self.assertEqual(self.comment.author, 1)

    def test_model_text(self):
        self.assertEqual(self.comment.text, 'testtext')

    def test_model_str(self):
        self.assertEqual(str(self.comment), '1')
