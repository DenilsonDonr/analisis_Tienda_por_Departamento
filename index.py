import pandas as pd
import matplotlib.pyplot as plt

# 01. Cargar el archivo en un DataFrame
df = pd.read_csv('Ventas_tienda_por_departamento.csv', sep=';', decimal='.', encoding='ISO-8859-1')

# 02. Crear un archivo CSV llamado "reporte-lima.csv" con los datos de las tiendas de "Lima"
df_lima = df[df['Tienda'] == 'Lima']
df_lima.to_csv('archivos/reporte-lima.csv', index=False)

# 03. Crear un archivo CSV llamado "reporte-provincia.csv" con los datos de las tiendas de "provincia" (todo lo que no sea Lima)
df_provincia = df[df['Tienda'] != 'Lima']
df_provincia.to_csv('archivos/reporte-provincia.csv', index=False)

# 04. Obtener el total de ventas por cada una de las marcas: Adidas, Asics y Nike
ventas_marcas = df[df['Marca'].isin(['Adidas', 'Asics', 'Nike'])]
total_ventas_marcas = ventas_marcas.groupby('Marca')['precio de venta S/'].sum()
print("Total de ventas por marca:")
print(total_ventas_marcas)

# 05. Construir un gráfico estadístico con los datos de la operación anterior
total_ventas_marcas.plot(kind='bar', color=['blue', 'green', 'red'])
plt.title('Total de Ventas por Marca')
plt.ylabel('Total de Ventas (S/)')
plt.xlabel('Marca')
plt.xticks(rotation=0)
plt.savefig('archivos/ventas_por_marca.png')  # Guardar el gráfico
plt.show()

# 06. Determinar cuál es el precio más bajo del producto de la categoría "Pantalon"
precio_min_pantalon = df[df['Categoria'] == 'Pantalon']['precio de venta S/'].min()
print(f"El precio más bajo de un Pantalón es: S/{precio_min_pantalon}")

# 07. Calcular el promedio de precio de los productos de la categoría "Ropa interior"
promedio_ropa_interior = df[df['Categoria'] == 'Ropa interior']['precio de venta S/'].mean()
print(f"El promedio de precio de Ropa Interior es: S/{promedio_ropa_interior}")

# 08. Calcular el precio más alto de los productos de la categoría "Zapatillas"
precio_max_zapatillas = df[df['Categoria'] == 'Zapatillas']['precio de venta S/'].max()
print(f"El precio más alto de unas Zapatillas es: S/{precio_max_zapatillas}")

# 09. ¿Cuántas ventas se realizaron entre el 15 y 18 de julio del 2025?
# Convertir la columna de fecha al formato adecuado para filtrar por fechas
df['Fecha'] = pd.to_datetime(df['Fecha'], format='%d/%m/%Y')
ventas_julio = df[(df['Fecha'] >= '2025-07-15') & (df['Fecha'] <= '2025-07-18')]
print(f"Ventas entre el 15 y 18 de julio de 2025: {len(ventas_julio)}")

# 10. Crear un gráfico que muestre la cantidad de ventas en función del género Femenino, Masculino y Unisex
ventas_por_genero = df['Género'].value_counts()
ventas_por_genero.plot(kind='bar', color=['purple', 'orange', 'yellow'])
plt.title('Cantidad de Ventas por Género')
plt.ylabel('Cantidad de Ventas')
plt.xlabel('Género')
plt.xticks(rotation=0)
plt.savefig('archivos/ventas_por_genero.png')  # Guardar el gráfico
plt.show()
