from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from .db_config import AsyncSessionLocal


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session
