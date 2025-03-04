# scripts/database/load_initial_data.py
import pandas as pd
from sqlalchemy import create_engine
from app.models import Producto, Base

def main():
    # Configurar conexión
    engine = create_engine("postgresql://user:password@db:5432/inventario")
    Base.metadata.create_all(engine)

    # Leer y limpiar datos
    df = pd.read_excel("Inventario_Sayer.xlsx")
    df["CODIGO_SAYER"] = df.apply(
        lambda row: f"{row['CODIGO-SAYS']}-AGUA" if "agua" in row["Productos"].lower() else f"{row['CODIGO-SAYS']}-MADERA",
        axis=1
    )

    # Cargar a PostgreSQL
    df.to_sql("productos", engine, if_exists="append", index=False)

if __name__ == "__main__":
    main()