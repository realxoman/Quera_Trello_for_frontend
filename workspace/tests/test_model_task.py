from django.test import TestCase
from workspace.models import Workspace, Project, Board, Task
from django.contrib.auth import get_user_model


class TaskTest(TestCase):
    def setUp(self):
        # create a test user
        self.user = get_user_model().objects.create_user(
            username="testuser", password="testpassword"
        )

        self.workspace = Workspace(name="testname", creator=self.user)

        self.project = Project(workspace=self.workspace)

        self.board = Board(project=self.project, name="testname")

        self.task = Task(
            board=self.board,
            name="testname",
            description="testtext",
            priority=1,
            order=2,
        )

    def test_model_name(self):
        self.assertEqual(self.task.name, "testname")

    def test_model_description(self):
        self.assertEqual(self.task.description, "testtext")

    def test_model_priority(self):
        self.assertEqual(self.task.priority, 1)

    def test_model_order(self):
        self.assertEqual(self.task.order, 2)

    def test_model_str(self):
        self.assertEqual(str(self.task), "testname")
