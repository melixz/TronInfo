from fastapi import APIRouter, Depends, HTTPException, Query
from .schemas import TronRequestCreate, TronInfo, TronRequestOut
from .dependencies import get_tron_service
from sqlalchemy.orm import Session
from src.config.database.db_helper import get_db
from .repository import TronRepository

router = APIRouter(prefix="/tron", tags=["tron"])


@router.post("/", response_model=TronInfo)
def get_tron_info(request: TronRequestCreate, tron_service=Depends(get_tron_service)):
    try:
        return tron_service.get_tron_info(request.address)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/requests", response_model=list[TronRequestOut])
def get_requests(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, gt=0),
    db: Session = Depends(get_db),
):
    repository = TronRepository(db)
    return repository.get_requests(skip=skip, limit=limit)
