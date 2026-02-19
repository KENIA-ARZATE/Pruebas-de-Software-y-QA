"""
Menu principal que integra las clases.
"""
from Hotels import Hotel
from customer import Customer
from reservation import Reservation

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
            reservas = res_manager.display_reservations()
            hoteles = hotel_manager.display_hotels()
            clientes = cust_manager.display_customers()
            
            print("\n" + "="*70)
            print(f"{'ID Res.':<10} | {'Cliente':<20} | {'Hotel':<20}")
            print("-" * 70)
            
            for r in reservas:
                # nombre del cliente usando el ID guardado
                cliente_obj = next((c for c in clientes if str(c['id']) == str(r['customer_id'])), None)
                nombre_cliente = cliente_obj['name'] if cliente_obj else "Desconocido"
                
                # nombre del hotel usando el ID guardado
                hotel_obj = next((h for h in hoteles if str(h['id']) == str(r['hotel_id'])), None)
                nombre_hotel = hotel_obj['name'] if hotel_obj else "Desconocido"
                
                print(f"{r['res_id']:<10} | {nombre_cliente:<20} | {nombre_hotel:<20}")
            print("="*70)

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

def menu_reservaciones(res_manager, hotel_manager, cust_manager):
    """Interfaz para gestionar reservaciones vinculando IDs."""
    while True:
        print("\n--- GESTIÓN DE RESERVACIONES ---")
        print("1. Crear Reservación")
        print("2. Cancelar Reservación")
        print("3. Mostrar Reservaciones")
        print("4. Regresar")
        op = input("Seleccione una opción: ")

        if op == "1":
            r_id = input("ID Reservación: ")
            c_id = input("ID Cliente: ")
            h_id = input("ID Hotel: ")
            # Se pasan las listas actuales para validar existencia (Req 5)
            res_manager.create_reservation(
                r_id, c_id, h_id,
                cust_manager.display_customers(),
                hotel_manager.display_hotels()
            )
        elif op == "2":
            r_id = input("ID de reservación a cancelar: ")
            res_manager.cancel_reservation(r_id)
        elif op == "3":
            reservas = res_manager.display_reservations()
            print("\nID Res. | ID Cliente | ID Hotel")
            for r in reservas:
                print(f"{r['res_id']} | {r['customer_id']} | {r['hotel_id']}")
        elif op == "4":
            break


def main():
    """Punto de entrada principal del sistema."""
    hotel_api = Hotel()
    customer_api = Customer()
    reservation_api = Reservation()

    while True:
        print("\n=== SISTEMA DE RESERVACIONES HOTELES TEC ===")
        print("1. Administrar Hoteles")
        print("2. Administrar Clientes")
        print("3. Administrar Reservaciones")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_hoteles(hotel_api)
        elif opcion == "2":
            menu_clientes(customer_api)
        elif opcion == "3":
            menu_reservaciones(reservation_api, hotel_api, customer_api)
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
