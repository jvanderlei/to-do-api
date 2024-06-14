from dataclasses import dataclass


@dataclass(init=False, eq=True, frozen=True)
class TaskStatus:
    task_status_id: int
    task_status_name: str

    def __init__(
            self,
            task_status_id: int,
            task_status_name: str
    ):
        if task_status_id not in [1, 2, 3]:
            raise ValueError("Código de status deve ser 1, 2 ou 3!")
        if task_status_id == 1 and task_status_name != "Pending":
            raise ValueError("Status deve ser pendente quando código for 1!")
        if task_status_id == 2 and task_status_name != "Finished":
            raise ValueError("Status deve ser concluído quando código for 2!")
        if task_status_id == 3 and task_status_name != "Canceled":
            raise ValueError("Status deve ser cancelado quando código for 3!")
        object.__setattr__(self, "task_status_id", task_status_id)
        object.__setattr__(self, "task_status_name", task_status_name)
