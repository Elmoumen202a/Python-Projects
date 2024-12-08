import unittest
from main import CarRental

class TestCarRental(unittest.TestCase):
    def setUp(self):
        """
        Set up a rental system with some cars for testing.
        """
        self.rental_system = CarRental()
        self.rental_system.add_car(1, "Toyota Corolla", 40)
        self.rental_system.add_car(2, "Honda Civic", 50)

    def test_add_car(self):
        """
        Test if a new car can be added successfully.
        """
        self.rental_system.add_car(3, "Tesla Model 3", 100)
        self.assertEqual(len(self.rental_system.cars), 3)

    def test_rent_car(self):
        """
        Test renting a car.
        """
        result = self.rental_system.rent_car(1)
        self.assertEqual(result, "Car 1 has been rented out.")
        self.assertTrue(self.rental_system.cars[0].is_rented)

    def test_return_car(self):
        """
        Test returning a car.
        """
        self.rental_system.rent_car(1)
        result = self.rental_system.return_car(1)
        self.assertEqual(result, "Car 1 has been returned.")
        self.assertFalse(self.rental_system.cars[0].is_rented)

    def test_rent_unavailable_car(self):
        """
        Test renting a car that is already rented.
        """
        self.rental_system.rent_car(1)
        result = self.rental_system.rent_car(1)
        self.assertEqual(result, "Car 1 is not available.")

if __name__ == "__main__":
    unittest.main()
