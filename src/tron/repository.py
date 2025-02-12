from sqlalchemy.orm import Session
from .models import TronRequest


class TronRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_request(self, address: str) -> TronRequest:
        tron_request = TronRequest(address=address)
        self.db.add(tron_request)
        self.db.commit()
        self.db.refresh(tron_request)
        return tron_request

    def get_requests(self, skip: int = 0, limit: int = 10):
        return self.db.query(TronRequest).offset(skip).limit(limit).all()
