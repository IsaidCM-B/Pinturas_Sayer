from sqlalchemy.orm import Session
from app.models import Producto

class InventoryManager:
    def __init__(self, db: Session):
        self.db = db
    
    def add_product(self, clave: str, nombre: str, cantidad: int, precio: float):
        nuevo_producto = Producto(
            clave=clave,
            nombre=nombre,
            cantidad=cantidad,
            precio=precio
        )
        self.db.add(nuevo_producto)
        self.db.commit()
        return nuevo_producto
    
    def get_stock(self, clave: str):
        return self.db.query(Producto).filter(Producto.clave == clave).first()
    
    def update_stock(self, clave: str, delta: int):
        producto = self.get_stock(clave)
        if producto:
            producto.cantidad += delta
            self.db.commit()
        return producto