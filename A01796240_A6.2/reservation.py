"""
Modulo para la gestion de reservaciones.
"""
import json
import os


class Reservation:
    """Clase para manejar reservaciones vinculando Hoteles y Clientes."""

    def __init__(self, file_name="reservations.json"):
        base_path = os.path.dirname(__file__)
        self.file_path = os.path.join(base_path, file_name)
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        """Crea el archivo de reservaciones si no existe."""
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w', encoding='utf-8') as f:
                json.dump([], f)

    def create_reservation(self, res_id, customer_id, hotel_id,
                           customers, hotels):
        """
        Crea una reservacion validando que el cliente y el hotel existan.
        Maneja casos negativos de IDs no encontrados (Req 5).
        """
        # Validacion: ¿Existe el cliente? (Caso Negativo)
        if not any(str(c['id']) == str(customer_id) for c in customers):
            print(f"Error: Cliente {customer_id} no existe.")
            return

        # Validacion: ¿Existe el hotel? (Caso Negativo)
        if not any(str(h['id']) == str(hotel_id) for h in hotels):
            print(f"Error: Hotel {hotel_id} no existe.")
            return

        reservations = self.display_reservations()
        
        # Validacion: ¿ID de reserva duplicado? (Caso Negativo)
        if any(str(r['res_id']) == str(res_id) for r in reservations):
            print(f"Error: El ID de reservacion {res_id} ya existe.")
            return

        reservations.append({
            "res_id": str(res_id),
            "customer_id": str(customer_id),
            "hotel_id": str(hotel_id)
        })
        self._save_to_file(reservations)
        print(f"Reservacion {res_id} creada exitosamente.")

    def cancel_reservation(self, res_id):
        """Elimina una reservacion del archivo JSON."""
        reservations = self.display_reservations()
        updated = [r for r in reservations if str(r['res_id']) != str(res_id)]
        
        if len(updated) == len(reservations):
            print(f"Error: Reservacion {res_id} no encontrada.")
            return
        
        self._save_to_file(updated)
        print(f"Reservacion {res_id} cancelada.")

    def display_reservations(self):
        """Retorna la lista de reservaciones."""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def _save_to_file(self, data):
        """Guarda los cambios en el archivo JSON."""
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
