from datetime import datetime
from pydantic import BaseModel


class TronInfo(BaseModel):
    address: str
    trx_balance: float
    bandwidth: int
    energy: int

    class Config:
        from_attributes = True


class TronRequestCreate(BaseModel):
    address: str


class TronRequestOut(BaseModel):
    id: int
    address: str
    requested_at: datetime

    class Config:
        from_attributes = True
