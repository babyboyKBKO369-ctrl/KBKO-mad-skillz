"""Base database models."""

from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, String
from kbko_core.database.base import Base


class BaseModel(Base):
    """Base model for all database models."""

    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
