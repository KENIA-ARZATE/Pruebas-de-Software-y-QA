"""Modulo de pruebas unitarias."""
import unittest
import os
from reservation import Reservation


class TestReservation(unittest.TestCase):
    """Casos de prueba para la clase."""
    def setUp(self):
        """Configuración inicial antes de cada prueba."""
        self.test_file = "test_reservations.json"
        self.res_sys = Reservation(self.test_file)
        # Datos de ejemplo para las validaciones
        self.mock_customers = [
            {
                "id": "C1",
                "name": "Klag",
                "email": "k@mail.com"
            }
        ]
        self.mock_hotels = [
            {
                "id": "H1",
                "name": "Tec Hotel",
                "location": "Toluca",
                "rooms": 10
            }
        ]

    def tearDown(self):
        """Limpieza después de cada prueba."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_create_reservation_success(self):
        """Caso Positivo: Crear una reservación válida."""
        self.res_sys.create_reservation(
            "R1", "C1", "H1", self.mock_customers, self.mock_hotels)
        self.assertTrue(os.path.exists(self.test_file))

    def test_create_reservation_invalid_customer(self):
        """Caso Negativo 1: Cliente no existe."""
        self.res_sys.create_reservation(
            "R2", "999", "H1", self.mock_customers, self.mock_hotels)
        res = self.res_sys.display_reservations()
        self.assertEqual(len(res), 0)

    def test_create_reservation_invalid_hotel(self):
        """Caso Negativo 2: Hotel no existe."""
        self.res_sys.create_reservation(
            "R3", "C1", "999", self.mock_customers, self.mock_hotels)
        res = self.res_sys.display_reservations()
        self.assertEqual(len(res), 0)

    def test_cancel_non_existent_reservation(self):
        """Caso Negativo 3: Cancelar algo que no existe."""
        # Esto prueba que el programa maneje el error sin tronar
        self.res_sys.cancel_reservation("R999")
