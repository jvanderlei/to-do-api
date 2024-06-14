from datetime import datetime

from pydantic import BaseModel, Field, ConfigDict

from domain.Entities.Task import Task
from infra.Data.TaskStatusDTO import TaskStatusDTO


class TaskReadModel(BaseModel):
    task_id: int = Field(example=345)
    task_name: str = Field(example="Study DDD")
    task_description: str = Field(example="Study the Domain Driven Design book")
    task_status_name: str = Field(example="Peding")
    task_due_to: datetime = Field(example="2024-06-15")


class TaskCreateModel(BaseModel):
    task_name: str = Field(example="Study DDD")
    task_description: str = Field(example="Study the Domain Driven Design book")
    task_due_to: datetime = Field(example="2024-06-15")


class TaskUpdateModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    task_name: str = Field(example="Study DDD")
    task_description: str = Field(example="Study the Domain Driven Design book")
    task_status_id: int = Field(ge=1, example=3)
    task_due_to: datetime = Field(example="2024-06-15")



    @staticmethod
    def from_entity(task: Task) -> "TaskReadModel":
        task_status_dto = TaskStatusDTO(
            task_status_id=task.task_status.task_status_id,
            task_status_name=task.task_status.task_status_name
        )
        return TaskReadModel(
            task_id=task.task_id,
            task_name=task.task_name,
            task_description=task.task_description,
            task_status_id=task_status_dto,
            task_due_to=task.task_due_to
        )
