import unittest
from engine.tire import Tire

class TestTire(unittest.TestCase):
    def test_carrigan_needs_service(self):
        tire = Tire(datetime.today().date())
        tire_type = "Carrigan"
        tire_wear = [0.9, 0.8, 0.85, 0.95]
        self.assertTrue(tire.needs_service(tire_type, tire_wear))

    def test_carrigan_does_not_need_service(self):
        tire = Tire(datetime.today().date())
        tire_type = "Carrigan"
        tire_wear = [0.8, 0.7, 0.6, 0.5]
        self.assertFalse(tire.needs_service(tire_type, tire_wear))

    def test_octoprime_needs_service(self):
        tire = Tire(datetime.today().date())
        tire_type = "Octoprime"
        tire_wear = [0.9, 1.1, 0.85, 0.95]
        self.assertTrue(tire.needs_service(tire_type, tire_wear))

    def test_octoprime_does_not_need_service(self):
        tire = Tire(datetime.today().date())
        tire_type = "Octoprime"
        tire_wear = [0.8, 0.7, 0.6, 0.5]
        self.assertFalse(tire.needs_service(tire_type, tire_wear))

    def test_invalid_tire_type(self):
        tire = Tire(datetime.today().date())
        tire_type = "InvalidTireType"
        tire_wear = [0.9, 0.8, 0.85, 0.95]
        with self.assertRaises(ValueError):
            tire.needs_service(tire_type, tire_wear)

if __name__ == '__main__':
    unittest.main()
