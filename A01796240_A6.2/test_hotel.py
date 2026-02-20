import unittest
import os
from Hotels import Hotel

class TestHotel(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_hotels_db.json"
        self.hotel_sys = Hotel(self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_create_hotel_success(self):
        """Prueba creación exitosa."""
        self.hotel_sys.create_hotel("H1", "Hotel Tec", "Toluca", 10)
        self.assertEqual(len(self.hotel_sys.display_hotels()), 1)

    def test_create_hotel_duplicate(self):
        """Caso Negativo: ID Duplicado."""
        self.hotel_sys.create_hotel("H1", "Hotel A", "Toluca", 10)
        self.hotel_sys.create_hotel("H1", "Hotel B", "Toluca", 5)
        self.assertEqual(len(self.hotel_sys.display_hotels()), 1)

    def test_modify_hotel_full(self):
        """Prueba modificar nombre, ubicación y habitaciones."""
        self.hotel_sys.create_hotel("H1", "Original", "CDMX", 5)
        self.hotel_sys.modify_hotel("H1", name="Nuevo", location="Cancun", rooms=20)
        h = self.hotel_sys.display_hotels()[0]
        self.assertEqual(h['name'], "Nuevo")
        self.assertEqual(h['location'], "Cancun")
        self.assertEqual(h['rooms'], 20)

    def test_modify_hotel_not_found(self):
        """Caso Negativo: Modificar hotel inexistente."""
        self.hotel_sys.modify_hotel("999", name="Error")
        self.assertEqual(len(self.hotel_sys.display_hotels()), 0)

    def test_delete_hotel_success(self):
        """Prueba eliminar hotel existente."""
        self.hotel_sys.create_hotel("H1", "Hotel A", "Toluca", 10)
        self.hotel_sys.delete_hotel("H1")
        self.assertEqual(len(self.hotel_sys.display_hotels()), 0)

    def test_delete_hotel_not_found(self):
        """Caso Negativo: Eliminar hotel que no existe."""
        self.hotel_sys.delete_hotel("999")
        self.assertEqual(len(self.hotel_sys.display_hotels()), 0)

if __name__ == '__main__':
    unittest.main()
