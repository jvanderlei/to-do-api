from datetime import datetime

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from domain.Entities.Task import Task
from infra.Data import TaskStatusDTO
from infra.Data.Base import Base
from use_cases.task_usecase_model import TaskReadModel


class TaskDTO(Base):
    __tablename__ = "todo_tasks"
    task_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    task_name: Mapped[str] = mapped_column(String(90), nullable=False)
    task_description: Mapped[str] = mapped_column(String(300), nullable=True)
    task_due_to: Mapped[datetime] = mapped_column(nullable=True)
    task_status_id: Mapped[int] = mapped_column(ForeignKey("status_todo_tasks.task_status_id"))
    task_status: Mapped["TaskStatusDTO"] = relationship("TaskStatusDTO")

    def to_entity(self) -> Task:
        return Task(
            task_id=self.task_id,
            task_name=self.task_name,
            task_description=self.task_description,
            task_due_to=self.task_due_to,
            task_status=self.task_status.to_entity()
        )

    def to_read_model(self) -> TaskReadModel:
        task_status_entity = self.task_status.to_entity()
        return TaskReadModel(
            task_id=self.task_id,
            task_name=self.task_name,
            task_description=self.task_description,
            task_due_to=self.task_due_to,
            task_status_name=task_status_entity.task_status_name
        )

    @staticmethod
    def from_entity(task: Task) -> "TaskDTO":
        return TaskDTO(
            task_id=task.task_id,
            task_name=task.task_name,
            task_description=task.task_description,
            task_due_to=task.task_due_to,
            task_status_id=task.task_status.task_status_id
        )
