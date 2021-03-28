from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends
from project_name.db import get_db
from project_name.example import service
from project_name.example.schemas import Example

router = APIRouter()


@router.get("/examples/", response_model=Example)
async def example(db: Session = Depends(get_db)) -> Example:
    return service.get_example(db)
