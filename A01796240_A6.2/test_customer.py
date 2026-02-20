"""
Pruebas unitarias para la clase Customer.
"""
import unittest
import os
import json
from customer import Customer


class TestCustomer(unittest.TestCase):
    """Casos de prueba para validar la gestion de clientes."""

    def setUp(self):
        """Configuracion inicial antes de cada prueba."""
        self.test_file = "test_customers.json"
        self.cust_sys = Customer(self.test_file)

    def tearDown(self):
        """Limpieza de archivos temporales de prueba."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_create_customer_success(self):
        """Caso Positivo: Crear un cliente correctamente."""
        self.cust_sys.create_customer("C1", "KLAG", "klag@mail.com")
        customers = self.cust_sys.display_customers()
        self.assertEqual(len(customers), 1)
        self.assertEqual(customers[0]['name'], "KLAG")

    def test_create_customer_duplicate(self):
        """Caso Negativo: No permitir IDs duplicados (Req 5)."""
        self.cust_sys.create_customer("C1", "User1", "u1@mail.com")
        self.cust_sys.create_customer("C1", "User2", "u2@mail.com")
        customers = self.cust_sys.display_customers()
        self.assertEqual(len(customers), 1)

    def test_delete_customer_success(self):
        """Caso Positivo: Eliminar un cliente existente."""
        self.cust_sys.create_customer("C1", "User1", "u1@mail.com")
        self.cust_sys.delete_customer("C1")
        self.assertEqual(len(self.cust_sys.display_customers()), 0)

    def test_delete_customer_not_found(self):
        """Caso Negativo: Intentar eliminar un ID que no existe."""
        self.cust_sys.create_customer("C1", "User1", "u1@mail.com")
        self.cust_sys.delete_customer("999")
        # El cliente original debe seguir ahi
        self.assertEqual(len(self.cust_sys.display_customers()), 1)

    def test_modify_customer_success(self):
        """Caso Positivo: Modificar datos de un cliente."""
        self.cust_sys.create_customer("C1", "Original", "o@mail.com")
        self.cust_sys.modify_customer("C1", name="Modificado")
        customers = self.cust_sys.display_customers()
        self.assertEqual(customers[0]['name'], "Modificado")

    def test_modify_customer_not_found(self):
        """Caso Negativo: Modificar un cliente inexistente."""
        self.cust_sys.modify_customer("999", name="Error")
        # El archivo deberia seguir vacio o sin cambios
        self.assertEqual(len(self.cust_sys.display_customers()), 0)


if __name__ == '__main__':
    unittest.main()