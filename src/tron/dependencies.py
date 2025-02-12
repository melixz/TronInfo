from fastapi import Depends
from sqlalchemy.orm import Session
from src.config.database.db_helper import get_db
from .repository import TronRepository
from .service import TronService


def get_tron_service(db: Session = Depends(get_db)) -> TronService:
    repository = TronRepository(db)
    return TronService(repository)
