from app.database import get_db
from app.modules.inventory import InventoryManager
import pandas as pd

def main():
    db = next(get_db())
    manager = InventoryManager(db)
    
    while True:
        print("\n=== Gestión de Inventario Sayer ===")
        print("1. Agregar producto")
        print("2. Consultar stock")
        print("3. Actualizar inventario")
        print("4. Exportar a Excel")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            clave = input("Clave del producto: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad inicial: "))
            precio = float(input("Precio: "))
            manager.add_product(clave, nombre, cantidad, precio)
            print("✅ Producto registrado!")
        
        elif opcion == "2":
            clave = input("Clave a consultar: ")
            producto = manager.get_stock(clave)
            if producto:
                print(f"Stock: {producto.cantidad} unidades")
            else:
                print("❌ Producto no encontrado")
        
        elif opcion == "3":
            clave = input("Clave del producto: ")
            delta = int(input("Cambio en stock (+/-): "))
            manager.update_stock(clave, delta)
            print("Inventario actualizado")
        
        elif opcion == "4":
            productos = db.query(Producto).all()
            df = pd.DataFrame([(p.clave, p.nombre, p.cantidad) for p in productos],
                            columns=["Clave", "Producto", "Stock"])
            df.to_excel("inventario.xlsx", index=False)
            print("📊 Excel generado: inventario.xlsx")
        
        elif opcion == "5":
            break

if __name__ == "__main__":
    main()