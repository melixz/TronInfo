from fastapi import APIRouter, Depends, HTTPException, Query
from .schemas import TronRequestCreate, TronInfo, TronRequestOut
from .dependencies import get_tron_service
from sqlalchemy.ext.asyncio import AsyncSession
from src.config.database.db_config import get_db
from .repository import TronRepository
from tronpy import Tron

router = APIRouter(prefix="/tron", tags=["tron"])


@router.post("/", response_model=TronInfo)
async def get_tron_info(
    request: TronRequestCreate, tron_service=Depends(get_tron_service)
):
    try:
        return await tron_service.get_tron_info(request.address)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/requests", response_model=list[TronRequestOut])
async def get_requests(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, gt=0),
    db: AsyncSession = Depends(get_db),
):
    repository = TronRepository(db)
    return await repository.get_requests(skip=skip, limit=limit)


@router.get("/generate_address")
async def generate_tron_address():
    client = Tron(network="nile")
    wallet = client.generate_address()
    return {
        "base58check_address": wallet["base58check_address"],
        "hex_address": wallet["hex_address"],
    }
