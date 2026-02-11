# pylint: disable=invalid-name
"""
Módulo para calcular el costo total de ventas a partir de archivos JSON.
"""

import sys
import json
import time


def load_json_data(file_path):
    """
    Carga y retorna los datos de un archivo JSON.
    Maneja errores si el archivo no existe o el formato es inválido.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as error:
        print(f"Error al procesar {file_path}: {error}")
        return None


def calculate_total_sales(catalogue, sales):
    """
    Calcula el costo total basado en el catálogo de precios y ventas.
    Soporta variaciones en nombres de llaves (product, title, description).
    """
    total_cost = 0
    price_map = {}

    # Mapear catálogo: busca llaves comunes en archivos de prueba
    for item in catalogue:
        # Intenta obtener el nombre del producto por varias llaves comunes
        name = item.get('product') or item.get('title') or \
            item.get('description') or item.get('Description')
        # Intenta obtener el precio o costo
        price = item.get('price') or item.get('cost') or item.get('Price', 0)

        if name is not None:
            price_map[name] = price

    # Procesar ventas y manejar datos inválidos
    for sale in sales:
        product = sale.get('product') or sale.get('title') or \
            sale.get('item') or sale.get('Product')
        quantity = sale.get('quantity') or sale.get('Quantity') or \
            sale.get('amount', 0)

        if product in price_map:
            total_cost += price_map[product] * quantity
        else:
            print(f"Error: Producto '{product}' no encontrado en catálogo.")

    return total_cost


def main():
    """
    Función principal que coordina la ejecución del programa.
    """
    start_time = time.time()

    # Verificar que se pasen los dos parámetros requeridos
    if len(sys.argv) != 3:
        print("Uso: python computeSales.py catálogo.json ventas.json")
        return

    catalogue_file = sys.argv[1]
    sales_file = sys.argv[2]

    # Cargar archivos
    catalogue = load_json_data(catalogue_file)
    sales = load_json_data(sales_file)

    if catalogue is not None and sales is not None:
        total = calculate_total_sales(catalogue, sales)
        elapsed_time = time.time() - start_time

        # Formatear resultados
        results = (
            f"{'='*30}\n"
            f"RESULTADOS DE VENTAS\n"
            f"{'='*30}\n"
            f"Total Ventas: ${total:,.2f}\n"
            f"Tiempo de ejecución: {elapsed_time:.4f} segundos\n"
            f"{'='*30}\n"
        )

        # Imprimir en pantalla y guardar en archivo
        print(results)
        with open("SalesResults.txt", "w", encoding="utf-8") as out_file:
            out_file.write(results)


if __name__ == "__main__":
    main()
