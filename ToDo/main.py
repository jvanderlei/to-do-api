import logging
from logging import config
from typing import Iterator, List

import uvicorn
from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from domain.Interfaces.TaskRepository import TaskRepository
from infra.Data.TaskRepository import (
    TaskRepositoryImpl
)
from infra.Data.database import SessionLocal, create_tables
from use_cases.task_usecase import TaskUseCase, TaskUseCaseImpl
from use_cases.task_usecase_model import TaskReadModel, TaskCreateModel, TaskUpdateModel

config.fileConfig("logging.conf", disable_existing_loggers=False)
logger = logging.getLogger(__name__)

app = FastAPI()

create_tables()


def get_session() -> Iterator[Session]:
    """Get a session from the database."""
    session: Session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


def task_usecase(session: Session = Depends(get_session)) -> TaskUseCaseImpl:
    task_repository: TaskRepository = TaskRepositoryImpl(session)
    return TaskUseCaseImpl(task_repository)


@app.post(
    "/tasks",
    response_model=TaskReadModel,
    status_code=status.HTTP_201_CREATED
)
async def create_task(
        data: TaskCreateModel,
        task_usecase: TaskUseCase = Depends(task_usecase)
):
    try:
        task = task_usecase.create_task(data)
    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    return task


@app.put(
    "/tasks/{id}",
    response_model=TaskReadModel,
    status_code=status.HTTP_202_ACCEPTED
)
async def update_task(
        id: int,
        data: TaskUpdateModel,
        task_usecase: TaskUseCase = Depends(task_usecase)
):
    try:
        task = task_usecase.update_task(id, data)
    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    return task


@app.delete(
    "/tasks/{id}",
    response_model=TaskReadModel,
    status_code=status.HTTP_200_OK
)
async def delete_task(
        id: int,
        task_usecase: TaskUseCase = Depends(task_usecase)
):
    try:
        task = task_usecase.delete_task(id)
    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    return task


@app.get(
    "/tasks",
    response_model=List[TaskReadModel],
    status_code=status.HTTP_200_OK
)
async def get_tasks_list(
        task_usecase: TaskUseCase = Depends(task_usecase)
):
    try:
        task_list = task_usecase.fetch_task_list()
    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    return task_list


@app.patch(
    "/tasks/{id}/complete",
    response_model=TaskReadModel,
    status_code=status.HTTP_200_OK
)
async def complete_task(
        id: int,
        task_usecase: TaskUseCase = Depends(task_usecase)
):
    try:
        task = task_usecase.complete_task(task_id=id)
    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    return task


# @app.get(
#     "/metrics"
# )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
