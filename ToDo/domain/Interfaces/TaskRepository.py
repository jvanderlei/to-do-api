from abc import ABC, abstractmethod
from typing import Optional

from domain.Entities.Task import Task


class TaskRepository(ABC):
    @abstractmethod
    def create_task(self, task: Task) -> Optional[Task]:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, task_id: int) -> Optional[Task]:
        raise NotImplementedError

    @abstractmethod
    def delete_task(self, task_id: int) -> Optional[Task]:
        raise NotImplementedError

    @abstractmethod
    def update_task(self, task: Task) -> Optional[Task]:
        raise NotImplementedError

    @abstractmethod
    def get_task_list(self) -> Optional[list[Task]]:
        raise NotImplementedError


