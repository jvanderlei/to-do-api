import datetime

from domain.ValueObjects import TaskStatus


class Task:
    def __init__(
            self,
            task_id: int,
            task_name: str,
            task_description: str,
            task_due_to: datetime,
            task_status: TaskStatus
    ):
        self.task_id: int = task_id
        self.task_name: str = task_name
        self.task_description: str = task_description
        self.task_due_to: str = task_due_to
        self.task_status: TaskStatus = task_status

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Task):
            return self.task_id == o.task_id

        return False




