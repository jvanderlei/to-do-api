from datetime import datetime

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from domain.Entities.Task import Task
from domain.ValueObjects.TaskStatus import TaskStatus
from infra.Data.DTO import TaskStatusDTO
from infra.Data.DTO.Base import Base


class TaskDTO(Base):
    __tablename__ = "todo_tasks"
    task_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    task_name: Mapped[str] = mapped_column(String(90), nullable=False)
    task_description: Mapped[str] = mapped_column(nullable=True)
    task_due_to: Mapped[datetime] = mapped_column(nullable=True)
    task_status_id: Mapped[int] = mapped_column(ForeignKey("status_todo_tasks.task_status_id"))
    task_status: Mapped["TaskStatusDTO"] = relationship("TaskStatusDTO")

    def to_entity(self) -> Task:
        return Task(
            task_id=self.task_id,
            task_name=self.task_name,
            task_status=TaskStatus(
                task_status_id=self.task_status.task_status_id,
                task_status_name=self.task_status.task_status_name
            ),
            task_description=self.task_description,
            task_due_to=self.task_due_to
        )


