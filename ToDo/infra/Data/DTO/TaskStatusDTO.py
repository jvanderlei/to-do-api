from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from domain.ValueObjects.TaskStatus import TaskStatus
from infra.Data.DTO.Base import Base


class TaskStatusDTO(Base):
    __tablename__ = "status_todo_tasks"
    task_status_id: Mapped[int] = mapped_column(primary_key=True)
    task_status_name: Mapped[int] = mapped_column(String(90), nullable=False)

    def to_entity(self) -> TaskStatus:
        return TaskStatus(
            task_status_id=self.task_status_id,
            task_status_name=self.task_status_name
        )
