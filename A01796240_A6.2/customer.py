"""
Modulo para la gestion de clientes.
"""
import json
import os

class Customer:
    """Clase para manejar la persistencia y logica de clientes."""
    def __init__(self, file_name="customers.json"):
        base_path = os.path.dirname(__file__)
        self.file_path = os.path.join(base_path, file_name)
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        """Asegura que el archivo JSON exista."""
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w', encoding='utf-8') as f:
                json.dump([], f)

    def create_customer(self, customer_id, name, email):
        """Crea un cliente y lo guarda en el archivo."""
        customers = self.display_customers()
        # Caso negativo: ID duplicado (Req 5)
        if any(str(c['id']) == str(customer_id) for c in customers):
            print(f"Error: El ID {customer_id} ya existe.")
            return
        
        customers.append({"id": str(customer_id), "name": name, "email": email})
        self._save_to_file(customers)
        print(f"Cliente {name} creado.")

    def delete_customer(self, customer_id):
        """Elimina un cliente por su ID."""
        customers = self.display_customers()
        updated = [c for c in customers if str(c['id']) != str(customer_id)]
        
        if len(updated) == len(customers):
            print(f"Error: Cliente {customer_id} no encontrado.")
            return
        
        self._save_to_file(updated)
        print(f"Cliente {customer_id} eliminado.")

    def modify_customer(self, customer_id, name=None, email=None):
        """Modifica la informacion de un cliente existente."""
        customers = self.display_customers()
        found = False
        for customer in customers:
            if str(customer['id']) == str(customer_id):
                if name:
                    customer['name'] = name
                if email:
                    customer['email'] = email
                found = True
                break
        
        if not found:
            print(f"Error: Cliente {customer_id} no existe.")
        else:
            self._save_to_file(customers)
            print(f"Cliente {customer_id} actualizado.")

    def display_customers(self):
        """Muestra la lista de clientes."""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def _save_to_file(self, data):
        """Guarda los datos en el archivo JSON."""
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)