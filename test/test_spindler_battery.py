import unittest
from datetime import datetime
from engine.model.spindler_battery import SpindlerBattery

class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        battery = SpindlerBattery(last_service_date)
        self.assertFalse(battery.needs_service())

    def test_needs_service_after_three_years(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        battery = SpindlerBattery(last_service_date)
        self.assertTrue(battery.needs_service())

if __name__ == '__main__':
    unittest.main()
