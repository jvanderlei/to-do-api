from datetime import datetime

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from infra.Data.Base import Base


class LogsDTO(Base):
    __tablename__ = "todo_logs"
    log_id: Mapped[int] = mapped_column(primary_key=True)
    log_level: Mapped[str] = mapped_column(String(30), nullable=False)
    log_content: Mapped[str] = mapped_column(String(300), nullable=False)
    log_generated: Mapped[datetime] = mapped_column()
