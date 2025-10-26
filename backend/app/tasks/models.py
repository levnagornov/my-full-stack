from sqlalchemy import ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime
from app.core.database import Base


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)


class CommitRun(Base):
    __tablename__ = "commit_runs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    static_data_implementation_date: Mapped[datetime] = mapped_column(
        DateTime, nullable=False)
    execution_date: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now, nullable=False)

    affected_tables: Mapped[list["AffectedTable"]] = relationship(
        "AffectedTable",
        back_populates="commit_run",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )


class AffectedTable(Base):
    __tablename__ = "affected_tables"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    commit_run_id: Mapped[int] = mapped_column(
        ForeignKey("commit_runs.id.id", ondelete="CASCADE"))

    commit_run: Mapped["CommitRun"] = relationship(
        "CommitRun",
        back_populates="affected_tables"
    )
