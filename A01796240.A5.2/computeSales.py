"""
Módulo para calcular el costo total de ventas a partir de archivos JSON.
Incluye manejo de errores y cálculo de tiempo de ejecución.
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
    """
    total_cost = 0
    # Crear diccionario de precios para búsqueda rápida O(1)
    price_map = {item.get('product'): item.get('price', 0)
                 for item in catalogue if 'product' in item}

    for sale in sales:
        product = sale.get('product')
        quantity = sale.get('quantity', 0)

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

    if len(sys.argv) != 3:
        print("Uso: python computeSales.py priceCatalogue.json salesRecord.json")
        return

    catalogue_file = sys.argv[1]
    sales_file = sys.argv[2]

    catalogue = load_json_data(catalogue_file)
    sales = load_json_data(sales_file)

    if catalogue is not None and sales is not None:
        total = calculate_total_sales(catalogue, sales)
        elapsed_time = time.time() - start_time

        # Formatear resultados según Req 2 y Req 7
        results = (
            f"{'='*30}\n"
            f"RESULTADOS DE VENTAS\n"
            f"{'='*30}\n"
            f"Total Ventas: ${total:,.2f}\n"
            f"Tiempo de ejecución: {elapsed_time:.4f} segundos\n"
            f"{'='*30}"
        )

        print(results)

        # Guardar en archivo SalesResults.txt
        with open("SalesResults.txt", "w", encoding="utf-8") as out_file:
            out_file.write(results)


if __name__ == "__main__":
    main()