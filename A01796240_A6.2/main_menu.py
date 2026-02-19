"""
Menu principal que integra las clases.
"""
from Hotels import Hotel
from customer import Customer

def menu_hoteles(hotel_manager):
    """Interfaz para administrar hoteles."""
    while True:
        print("\n--- GESTIÓN DE HOTELES ---")
        print("1. Crear Hotel")
        print("2. Eliminar Hotel")
        print("3. Mostrar Hoteles")
        print("4. Modificar Hotel")
        print("5. Regresar")
        op = input("Seleccione una opción: ")

        if op == "1":
            h_id = input("ID Hotel: ")
            nom = input("Nombre: ")
            ub = input("Ubicación: ")
            hab = input("Habitaciones: ")
            hotel_manager.create_hotel(h_id, nom, ub, hab)
        elif op == "2":
            h_id = input("ID del hotel a eliminar: ")
            hotel_manager.delete_hotel(h_id)
        elif op == "3":
            hoteles = hotel_manager.display_hotels()
            for h in hoteles:
                print(f"ID: {h['id']} | Nombre: {h['name']} | Hab: {h['rooms']}")
        elif op == "4":
            h_id = input("ID del hotel a modificar: ")
            nom = input("Nuevo nombre (vacío para omitir): ")
            ub = input("Nueva ubicación (vacío para omitir): ")
            hab = input("Nuevas habitaciones (vacío para omitir): ")
            hotel_manager.modify_hotel(h_id, nom, ub, hab)
        elif op == "5":
            break

def menu_clientes(cust_manager):
    """Interfaz para administrar clientes."""
    while True:
        print("\n--- GESTIÓN DE CLIENTES ---")
        print("1. Crear Cliente")
        print("2. Eliminar Cliente")
        print("3. Mostrar Clientes")
        print("4. Modificar Cliente")
        print("5. Regresar")
        op = input("Seleccione una opción: ")

        if op == "1":
            c_id = input("ID Cliente: ")
            nom = input("Nombre: ")
            email = input("Email: ")
            cust_manager.create_customer(c_id, nom, email)
        elif op == "2":
            c_id = input("ID a eliminar: ")
            cust_manager.delete_customer(c_id)
        elif op == "3":
            clientes = cust_manager.display_customers()
            for c in clientes:
                print(f"ID: {c['id']} | Nombre: {c['name']} | Email: {c['email']}")
        elif op == "4":
            c_id = input("ID a modificar: ")
            nom = input("Nuevo nombre (vacío para omitir): ")
            em = input("Nuevo email (vacío para omitir): ")
            cust_manager.modify_customer(c_id, nom, em)
        elif op == "5":
            break

def main():
    """Punto de entrada principal."""
    hotel_api = Hotel()
    customer_api = Customer()

    while True:
        print("\n=== SISTEMA DE RESERVACIONES TEC ===")
        print("1. Administrar Hoteles")
        print("2. Administrar Clientes")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_hoteles(hotel_api)
        elif opcion == "2":
            menu_clientes(customer_api)
        elif opcion == "3":
            print("Saliendo del sistema...")
            break

if __name__ == "__main__":
    main()
