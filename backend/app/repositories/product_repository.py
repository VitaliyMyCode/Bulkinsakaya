from sqlalchemy.orm import Session, joinedload
from typing import List, Optional
from ..models.product import Product
from ..schemas.product import ProductCreate, ProductUpdate

class ProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Product]:
        return self.db.query(Product).options(joinedload(Product.category)).all()
    
    def get_by_id(self, product_id: int) -> Optional[Product]:
        return (
            self.db.query(Product)
            .options(joinedload(Product.category))
            .filter(Product.id == product_id)
            .first()
            )
    
    def get_by_category(self, category_id: int) -> List[Product]:
        return (
            self.db.query(Product)
            .options(joinedload(Product.category))
            .filter(Product.category_id == category_id)
            .all()
            )
    
    def create(self, product_data: ProductCreate) -> Product:
        db_product = Product(**product_data.model_dump())
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product
    
    def get_multiple_by_ids(self, product_ids: List[int]) -> List[Product]:
        return(
            self.db.query(Product)
            .options(joinedload(Product.category))
            .filter(Product.id.in_(product_ids))
            .all()
        )
    
    def update_product(self, product_id: int, product_data: ProductUpdate) -> Product:
        db_product = self.db.query(Product).filter(Product.id == product_id).first()   
        update_data = product_data.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            setattr(db_product, field, value)
        self.db.commit()
        self.db.refresh(db_product)
        
        return db_product