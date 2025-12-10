from fastapi import status, APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import get_db
from ..services.product_service import ProductService
from ..schemas.product import ProductResponse, ProductListResponse, ProductCreate, ProductUpdate

router = APIRouter(
    prefix="/api/products",
    tags=["products"]
)

@router.get("", response_model=ProductListResponse, status_code=status.HTTP_200_OK)
def get_product(db: Session = Depends(get_db)):
    service = ProductService(db)
    return service.get_all_products()

@router.get("/{product_id}", response_model=ProductResponse, status_code=status.HTTP_200_OK)
def get_product_by_id(product_id: int, db: Session = Depends(get_db)):
    service = ProductService(db)
    return service.get_by_product_id(product_id)

@router.get("/category/{category_id}", response_model=ProductListResponse, status_code=status.HTTP_200_OK)
def get_product_by_category(category_id: int, db: Session = Depends(get_db)):
    service = ProductService(db)
    return service.get_products_by_category(category_id)

@router.post("", response_model=ProductResponse, status_code=status.HTTP_200_OK)
def create_product(product_in: ProductCreate, db: Session = Depends(get_db)):
    service = ProductService(db)
    return service.create_product(product_in)

@router.put("/{product_id}", response_model=ProductResponse, status_code=status.HTTP_200_OK)
def update_product(product_id: int, product_in: ProductUpdate, db: Session = Depends(get_db)):
    service = ProductService(db)
    return service.update_product(product_id, product_in)