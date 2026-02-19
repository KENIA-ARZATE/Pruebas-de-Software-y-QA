import json
import os

class Hotel:
    def __init__(self, file_path="hotels.json"):
        self.file_path = file_path
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as f:
                json.dump([], f)

    def create_hotel(self, hotel_id, name, location, rooms):
        try:
            hotels = self.display_hotels()
            if any(h['id'] == hotel_id for h in hotels):
                print(f"Error: Hotel ID {hotel_id} already exists.")
                return
            
            new_hotel = {
                "id": hotel_id,
                "name": name,
                "location": location,
                "rooms": int(rooms)
            }
            hotels.append(new_hotel)
            self._save_to_file(hotels)
        except ValueError:
            print("Error: Invalid data provided for rooms.")

    def display_hotels(self):
        try:
            with open(self.file_path, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            print("Error: Could not read file. Starting with empty list.")
            return []

    def _save_to_file(self, data):
        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=4)    
    pass

def main():
    """Función principal para ejecutar la interfaz de usuario."""
    sistema = Hotel("hotels.json")
    
    while True:
        print("\n--- SISTEMA DE RESERVACIONES (HOTELES) ---")
        print("1. Crear Hotel")
        print("2. Eliminar Hotel")
        print("3. Mostrar Hoteles")
        print("4. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            h_id = input("ID del Hotel: ")
            nombre = input("Nombre del Hotel: ")
            ubicacion = input("Ubicación: ")
            habitaciones = input("Número de habitaciones: ")
            sistema.create_hotel(h_id, nombre, ubicacion, habitaciones)
        
        elif opcion == "2":
            h_id = input("ID del hotel a eliminar: ")
            sistema.delete_hotel(h_id)
            
        elif opcion == "3":
            # (Lógica para mostrar hoteles que vimos antes)
            pass
            
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()