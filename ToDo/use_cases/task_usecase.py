from abc import ABC, abstractmethod
from typing import Optional, List

from domain.Entities.Task import Task
from domain.Interfaces.TaskRepository import TaskRepository
from domain.ValueObjects.TaskStatus import TaskStatus
from use_cases.task_usecase_model import TaskReadModel, TaskCreateModel, TaskUpdateModel


class TaskUseCase(ABC):
    task_repository: TaskRepository
    @abstractmethod
    def fetch_task_by_id(self, task_id: str) -> Optional[TaskReadModel]:
        raise NotImplementedError

    @abstractmethod
    def fetch_task_list(self) -> List[TaskReadModel]:
        raise NotImplementedError

    @abstractmethod
    def create_task(self, data: TaskCreateModel) -> Optional[TaskReadModel]:
        raise NotImplementedError

    @abstractmethod
    def delete_task(self, task_id: int):
        raise NotImplementedError

    @abstractmethod
    def update_task(self, task_id: int, data: TaskUpdateModel) -> Optional[TaskReadModel]:
        raise NotImplementedError


class TaskUseCaseImpl(TaskUseCase):
    def __init__(
            self,
            task_repository: TaskRepository
    ):
        self.task_repository = task_repository

    def create_task(self, data: TaskCreateModel) -> Optional[TaskReadModel]:
        try:
            task_status = TaskStatus(
                task_status_id=1,
                task_status_name="Pending"
            )
            task = Task(task_id=None, task_name=data.task_name, task_description=data.task_description, task_status=task_status, task_due_to=data.task_due_to)

            created_task = self.task_repository.create_task(task)
            if created_task:
                return TaskReadModel.from_entity(created_task)
            return None
        except Exception as e:
            print("Error creating task: {e}")
            return None


    def fetch_task_by_id(self, task_id: str) -> Optional[TaskReadModel]:
        pass

    def fetch_task_list(self) -> List[TaskReadModel]:
        pass

    def delete_task(self, task_id: int):
        pass

    def update_task(self, task_id: int, data: TaskUpdateModel) -> Optional[TaskReadModel]:
        pass