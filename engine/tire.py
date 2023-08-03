from car import Car
from datetime import datetime

class Tire(Car):
    def needs_service(self, tire_type, tire_wear):
        if tire_type == "Carrigan":
            return any(wear >= 0.9 for wear in tire_wear)
        elif tire_type == "Octoprime":
            return sum(tire_wear) >= 3
        else:
            raise ValueError("Invalid tire type")
