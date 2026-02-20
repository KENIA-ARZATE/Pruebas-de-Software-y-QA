# pylint: disable=duplicate-code
"""
Modulo para la gestion de Hoteles.
"""
import json
import os

class Hotel:
    """Clase que maneja la logica y persistencia de Hoteles."""
    def __init__(self, file_path="hotels.json"):
        base_path = os.path.dirname(__file__)
        self.file_path = os.path.join(base_path, file_path)
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        """Crea el archivo si no existe con encoding utf-8."""
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w', encoding='utf-8') as f:
                json.dump([], f)

    def create_hotel(self, hotel_id, name, location, rooms):
        """crea los hoteles."""
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
        """Muestra los hoteles."""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            print("Error: Could not read file. Starting with empty list.")
            return []

    def _save_to_file(self, data):
        with open(self.file_path, 'w', encoding='utf-8') as f:
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

        hotel_id = str(hotel_id)

        for hotel in hotels:
            if str(hotel['id']) == hotel_id:
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
