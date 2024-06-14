from typing import Optional

from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from domain.Entities.Task import Task
from domain.Interfaces.TaskRepository import TaskRepository
from infra.Data.TaskDTO import TaskDTO


class TaskRepositoryImpl(TaskRepository):
    def __init__(self, session: Session):
        self.session: Session = session

    def create_task(self, task: Task) -> Optional[Task]:
        try:
            task_dto = TaskDTO.from_entity(task)
            self.session.add(task_dto)
            self.session.commit()
            self.session.refresh(task_dto)  # Refresh to get the generated ID
            return task_dto.to_entity()
        except Exception as e:
            self.session.rollback()
            print(f"Error creating task: {e}")
            return None

    def find_by_id(self, task_id: int) -> Optional[Task]:
        try:
            task_dto = self.session.query(TaskDTO).filter_by(task_id=task_id).one()
            return task_dto.to_entity()
        except NoResultFound:
            return None
        except Exception as e:
            print(f"Error finding task by ID: {e}")
            return None

    def delete_task(self, task_id: int) -> Optional[Task]:
        try:
            task_dto = self.session.query(TaskDTO).filter_by(task_id=task_id).one()
            task = task_dto.to_entity()
            self.session.delete(task_dto)
            self.session.commit()
            return task
        except NoResultFound:
            return None
        except Exception as e:
            self.session.rollback()
            print(f"Error deleting task: {e}")
            return None

    def update_task(self, task: Task) -> Optional[Task]:
        try:
            task_dto = self.session.query(TaskDTO).filter_by(task_id=task.task_id).one()
            task_dto.task_name = task.task_name
            task_dto.task_description = task.task_description
            task_dto.task_due_to = task.task_due_to
            task_dto.task_status_id = task.task_status.task_status_id
            self.session.commit()
            return task_dto.to_entity()
        except NoResultFound:
            return None
        except Exception as e:
            self.session.rollback()
            print(f"Error updating task: {e}")
            return None

    def get_task_list(self) -> Optional[list[Task]]:
        try:
            task_dtos = self.session.query(TaskDTO).all()
            return [task_dto.to_entity() for task_dto in task_dtos]
        except Exception as e:
            print(f"Error retrieving task list: {e}")
            return None

