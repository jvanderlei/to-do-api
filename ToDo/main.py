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


