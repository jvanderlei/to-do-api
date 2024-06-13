import unittest

from domain.Entities.Task import Task
from domain.ValueObjects.TaskStatus import TaskStatus


class TestTask(unittest.TestCase):
    def test_task_constructor(self):
        task = Task(task_id=1, task_name="Domain for todo app", task_status=1,
                    task_description="Desenvolvimento da camada de Domain da API", task_due_to="2024-06-15")

        assert task.task_id == 1
        assert task.task_name == "Domain for todo app"
        assert task.task_status == 1
        assert task.task_description == "Desenvolvimento da camada de Domain da API"
        assert task.task_due_to == "2024-06-15"

    def test_task_status_constructor(self):
        task_status = TaskStatus(task_status_id=1, task_status_name="pending")

        assert task_status.task_status_id == 1
        assert task_status.task_status_name == "pending"

if __name__ == '__main__':
    unittest.main()
