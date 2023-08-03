from car import Car
from datetime import datetime

class SpindlerBattery(Car):
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 3)
        return service_threshold_date < datetime.today().date()
