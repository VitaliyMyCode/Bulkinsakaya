from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from ..services.category_services import CategoryService
from ..schemas.category import CategoryResponse, CategoryCreate

router = APIRouter(
    prefix="/api/categories",
    tags=["categories"]
)

@router.get("", response_model=List[CategoryResponse], status_code=status.HTTP_200_OK)
def get_categories(db: Session = Depends(get_db)):
    service = CategoryService(db)
    return service.get_all_categories()

@router.get('/{category_id}', response_model=CategoryResponse, status_code=status.HTTP_200_OK)
def get_category(category_id: int, db: Session = Depends(get_db)):
    service = CategoryService(db)
    return service.get_by_category_id(category_id)

@router.post("", response_model=CategoryResponse, status_code=status.HTTP_200_OK)
def create_category(category_in: CategoryCreate, db: Session = Depends(get_db)):
    service = CategoryService(db)
    return service.create_category(category_in)