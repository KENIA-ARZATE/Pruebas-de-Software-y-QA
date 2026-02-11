"""
Ejercicio 3: Word Count.
Cuenta la frecuencia de palabras distintas en un archivo de texto.
"""

import sys
import time


def get_words_from_file(file_path):
    """Lee el archivo y extrae las palabras limpias."""
    words_list = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # Req 2: Identificar palabras entre espacios
                raw_words = line.split()
                for word in raw_words:
                    # Limpieza basica de puntuacion
                    clean_word = word.strip('.,!?"()').lower()
                    if clean_word:
                        words_list.append(clean_word)
    except FileNotFoundError:
        print(f"Error: El archivo {file_path} no existe.")
    return words_list


def count_frequencies(words_list):
    """Cuenta cuantas veces aparece cada palabra sin librerias externas."""
    freq_dict = {}
    for word in words_list:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1
    return freq_dict


def main():
    """Funcion principal: coordina la lectura, conteo y salida."""
    if len(sys.argv) < 2:
        print("Uso: python word_count.py fileWithData.txt")
        return
    start_time = time.time()
    words = get_words_from_file(sys.argv[1])
    if not words:
        return
    frequencies = count_frequencies(words)
    end_time = time.time()
    elapsed = end_time - start_time
    # Preparar resultados alineados para pantalla y archivo
    output_lines = [f"{'PALABRA':<20} | {'FRECUENCIA':<10}", "-" * 33]
    # Ordenar alfabeticamente para consistencia
    for word in sorted(frequencies.keys()):
        output_lines.append(f"{word:<20} | {frequencies[word]:<10}")
    output_str = "\n".join(output_lines)
    output_str += f"\n\nTiempo de ejecucion: {elapsed:.6f} segundos\n"
    print(output_str)
    # Req 2: Guardar en WordCountResults.txt
    with open("WordCountResults.txt", "w", encoding='utf-8') as out_file:
        out_file.write(output_str)


if __name__ == "__main__":
    main()
