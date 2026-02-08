"""
Ejercicio 1: Compute Statistics.
Calcula estadísticas descriptivas a partir de un archivo.
"""

import sys
import time


def get_numbers_from_file(file_path):
    """Lee el archivo y extrae solo los datos numéricos válidos."""
    numbers = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    numbers.append(float(line.strip()))
                except ValueError:
                    print(f"Error: Dato inválido saltado: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: El archivo {file_path} no existe.")
    return numbers


def calculate_stats(numbers):
    """Realiza los cálculos estadísticos usando algoritmos básicos."""
    n_count = len(numbers)
    if n_count == 0:
        return None

    # Media
    mean_val = sum(numbers) / n_count

    # Mediana (Bubble Sort manual para Req 2)
    data = numbers[:]
    for i in range(n_count):
        for j in range(0, n_count - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

    if n_count % 2 == 0:
        median_val = (data[n_count // 2 - 1] + data[n_count // 2]) / 2
    else:
        median_val = data[n_count // 2]

    # Moda
    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1
    max_freq = max(counts.values())
    mode_val = [k for k, v in counts.items() if v == max_freq][0]

    # Varianza y Desviación Estándar
    variance_val = sum((x - mean_val) ** 2 for x in numbers) / n_count
    std_dev_val = variance_val ** 0.5

    return mean_val, median_val, mode_val, variance_val, std_dev_val


def main():
    """Función principal: coordina la ejecución y guarda resultados."""
    if len(sys.argv) < 2:
        print("Uso: python compute_statistics.py fileWithData.txt")
        return

    start_time = time.time()
    file_name = sys.argv[1]
    numbers = get_numbers_from_file(file_name)

    if not numbers:
        return

    stats = calculate_stats(numbers)
    mean, median, mode, var, std = stats

    end_time = time.time()
    elapsed = end_time - start_time

    results = (
        f"ARCHIVO: {file_name}\n"
        f"Media: {mean:.4f}\n"
        f"Mediana: {median:.4f}\n"
        f"Moda: {mode:.4f}\n"
        f"Varianza: {var:.4f}\n"
        f"Desviación Estándar: {std:.4f}\n"
        f"Tiempo: {elapsed:.6f} s\n"
    )

    print(results)
    # Req 2: Guardar en el archivo oficial
    with open("StatisticsResults.txt", "w", encoding='utf-8') as out_file:
        out_file.write(results)


if __name__ == "__main__":
    main()
