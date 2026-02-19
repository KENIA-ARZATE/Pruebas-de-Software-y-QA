import json
import os

class Hotel:
    def __init__(self, file_path="hotels.json"):
        base_path = os.path.dirname(__file__)
        self.file_path = os.path.join(base_path, file_path)
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

    def delete_hotel(self, hotel_id):
        """Elimina un hotel por su ID."""
        hotels = self.display_hotels()
        # Buscamos si el hotel existe
        updated_hotels = [h for h in hotels if h['id'] != hotel_id]
        
        if len(updated_hotels) == len(hotels):
            print(f"Error: Hotel con ID {hotel_id} no encontrado.")
            return
        
        self._save_to_file(updated_hotels)
        print(f"Hotel {hotel_id} eliminado exitosamente.")

    def modify_hotel(self, hotel_id, name=None, location=None, rooms=None):
        """Modificará la información de un hotel existente."""
        hotels = self.display_hotels()
        found = False
        
        for hotel in hotels:
            if hotel['id'] == hotel_id:
                if name:
                    hotel['name'] = name
                if location:
                    hotel['location'] = location
                if rooms is not None:
                    try:
                        hotel['rooms'] = int(rooms)
                    except ValueError:
                        print("Error: El número de habitaciones debe ser un entero.")
                        return
                found = True
                break
        
        if not found:
            print(f"Error: No se pudo modificar. ID {hotel_id} no existe.")
        else:
            self._save_to_file(hotels)
            print(f"Información del hotel {hotel_id} actualizada.")         
    pass

def main():
    """Función principal para ejecutar la interfaz de usuario."""
    sistema = Hotel("hotels.json")
    
    while True:
        print("\n--- SISTEMA DE RESERVACIONES (HOTELES) ---")
        print("1. Crear Hotel")
        print("2. Eliminar Hotel")
        print("3. Mostrar Hoteles")
        print("4. Modificar Hotel")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            h_id = input("ID del Hotel: ")
            nombre = input("Nombre del Hotel: ")
            ubicacion = input("Ubicación: ")
            habitaciones = input("Número de habitaciones: ")
            sistema.create_hotel(h_id, nombre, ubicacion, habitaciones)
            print("¡Archivo actualizado!")

        elif opcion == "2":
            h_id = input("ID del hotel a eliminar: ")
            sistema.delete_hotel(h_id)
            
        elif opcion == "3":
            hotels = sistema.display_hotels()
            if not hotels:
                print("No hay hoteles registrados.")
            else:
                print("\n--- HOTELES REGISTRADOS ---")
                for hotel in hotels:
                    print(f"ID: {hotel['id']}, Nombre: {hotel['name']}, Ubicación: {hotel['location']}, Habitaciones: {hotel['rooms']}")
            
        elif opcion == "4":
            h_id = input("ID del hotel a modificar: ")
            nombre = input("Nuevo nombre (dejar en blanco para no modificar): ")
            ubicacion = input("Nueva ubicación (dejar en blanco para no modificar): ")
            habitaciones = input("Nuevo número de habitaciones (dejar en blanco para no modificar): ")
            sistema.modify_hotel(h_id, name=nombre if nombre else None, location=ubicacion if ubicacion else None, rooms=habitaciones if habitaciones else None)
            
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()