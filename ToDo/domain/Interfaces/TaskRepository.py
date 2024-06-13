from abc import ABC
from typing import Optional

from domain.Entities import Task


class TaskRepository(ABC):
    def create_task(self, task: Task) -> Optional[Task]:
        raise NotImplementedError

    def find_by_id(self, task_id: int) -> Optional[Task]:
        raise NotImplementedError

    def delete_task(self, task_id: int) -> Optional[Task]:
        raise NotImplementedError

    def update_task(self, task: Task) -> Optional[Task]:
        raise NotImplementedError

    def get_task_list(self) -> Optional[list[Task]]:
        raise NotImplementedError


