import uvicorn
import logging
import os
from logging import config
from typing import Iterator, List

from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from domain.Entities.Task import Task
from domain.ValueObjects.TaskStatus import TaskStatus
from domain.Interfaces.TaskRepository import TaskRepository

from infra.Data.TaskRepository import (
    TaskRepositoryImpl
)

from infra.Data.database import SessionLocal, create_tables

from use_cases.task_usecase_model import TaskReadModel, TaskCreateModel, TaskUpdateModel
from use_cases.task_usecase import TaskUseCase, TaskUseCaseImpl


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

# @app.delete(
#     "/tasks/{id}"
# )
#
# @app.get(
#     "/tasks"
# )
#
# @app.patch(
#     "/tasks/{id}/complete"
# )
#
# @app.get(
#     "/metrics"
# )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)