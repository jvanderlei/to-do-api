import unittest

from infra.Data.TaskDTO import TaskDTO


class TestTaskDTO(unittest.TestCase):
    def test_read_model_create_entity(self):
        task_dto = TaskDTO(
            task_name='Create infra layer',
            task_description="Develop the infrastructure layer responsible for accessing Databases",
            task_due_to="2024-06-13 10:00:00",
            task_status=1,
        )


if __name__ == '__main__':
    unittest.main()
