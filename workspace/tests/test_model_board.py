from django.test import TestCase
from workspace.models import Workspace, Project, Board
from django.contrib.auth import get_user_model


class BoardTest(TestCase):

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
            workspace=self.workspace,
            name=1
        )

        self.board = Board(
            project=self.project,
            name='testname',
            order=1
        )

    def test_model_name(self):
        self.assertEqual(self.board.name, 'testname')

    def test_model_order(self):
        self.assertEqual(self.board.order, 1)

    def test_model_str(self):
        self.assertEqual(str(self.board), 'testname')
