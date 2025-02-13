from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import text
from .models import TronRequest


class TronRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_request(self, address: str):
        tron_request = TronRequest(address=address)
        self.db.add(tron_request)
        await self.db.commit()
        await self.db.refresh(tron_request)
        return tron_request

    async def get_requests(self, skip: int = 0, limit: int = 10):
        result = await self.db.execute(
            text(
                "SELECT * FROM tron_requests ORDER BY requested_at DESC LIMIT :limit OFFSET :skip"
            ),
            {"limit": limit, "skip": skip},
        )
        return result.fetchall()
