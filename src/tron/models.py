from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from src.config.database.db_config import Base


class TronRequest(Base):
    __tablename__ = "tron_requests"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, index=True, nullable=False)
    requested_at = Column(DateTime, default=datetime.utcnow, nullable=False)
