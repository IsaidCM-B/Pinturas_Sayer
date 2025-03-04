from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Producto(Base):
    __tablename__ = "productos"
    
    id = Column(Integer, primary_key=True, index=True)
    clave = Column(String(50), unique=True)
    codigo_barras = Column(String(20))
    nombre = Column(String(100))
    cantidad = Column(Integer, default=0)
    precio = Column(Float)
    proveedor = Column(String(50))

# Ejecutar en consola para crear tablas:
# from app.database import engine, Base
# Base.metadata.create_all(bind=engine)
