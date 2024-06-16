from abc import ABC, abstractmethod
from typing import Optional, List

from domain.Entities.Task import Task
from domain.Interfaces.TaskRepository import TaskRepository
from domain.ValueObjects.TaskStatus import TaskStatus
from use_cases.task_usecase_model import TaskReadModel, TaskCreateModel, TaskUpdateModel


class TaskUseCase(ABC):
    task_repository: TaskRepository

    @abstractmethod
    def complete_task(self, task_id: int) -> Optional[TaskReadModel]:
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
            task = Task(task_id=None, task_name=data.task_name,
                        task_description=data.task_description,
                        task_status=task_status,
                        task_due_to=data.task_due_to
                        )

            created_task = self.task_repository.create_task(task)
            if created_task:
                return TaskReadModel.from_entity(created_task)
            return None
        except Exception as e:
            print(f"Error creating task: {e}")
            return None

    def complete_task(self, task_id: int) -> Optional[TaskReadModel]:
        try:
            task = self.task_repository.find_by_id(task_id)
            task_status = self.task_repository.find_status_by_id(2)
            task.task_status = task_status
            completed_task = self.task_repository.update_task(task.task_id, task)
            if completed_task:
                return TaskReadModel.from_entity(completed_task)
            return None
        except Exception as e:
            print(f"Error creating task: {e}")
            return None



    def fetch_task_list(self) -> List[TaskReadModel]:
        try:
            task_list = self.task_repository.get_task_list()
            if task_list:
                return [TaskReadModel.from_entity(task) for task in task_list]
            return None
        except Exception as e:
            print(f"Error creating task: {e}")
            return None

    def delete_task(self, task_id: int):
        try:
            deleted_task = self.task_repository.delete_task(task_id)
            if deleted_task:
                return TaskReadModel.from_entity(deleted_task)
            return None
        except Exception as e:
            print(f"Error deleting task: {e}")
            return None

    def update_task(self, task_id: int, data: TaskUpdateModel) -> Optional[TaskReadModel]:
        try:
            task_status = self.task_repository.find_status_by_id(data.task_status_id)
            task = Task(task_id=task_id, task_name=data.task_name,
                        task_description=data.task_description,
                        task_status=task_status,
                        task_due_to=data.task_due_to
                        )
            updated_task = self.task_repository.update_task(task_id, task)
            if task:
                return TaskReadModel.from_entity(updated_task)
            return None
        except Exception as e:
            print(f"Error creating task: {e}")
            return None
