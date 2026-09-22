from django.test import TestCase
from .models import Task


class TaskModelTest(TestCase):
    def test_task_creation(self):
        task = Task.objects.create(
            title="Test task"
        )

        self.assertEqual(task.title, "Test task")
