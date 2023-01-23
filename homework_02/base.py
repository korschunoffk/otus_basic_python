from abc import ABC
from homework_02.exceptions import LowFuelError
from homework_02.exceptions import NotEnoughFuel

class Vehicle(ABC):
    weight = None
    started = False
    fuel = None
    fuel_consumption = None

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
                if self.fuel != 0:
                    self.started = True
                    print("engine is running")
                else:
                    raise LowFuelError

    def move(self,distance):
        self.distance = distance
        remaining = self.fuel - self.distance * self.fuel_consumption
        if remaining <= self.fuel and remaining >= 0:
            self.fuel = remaining
        else:
            raise NotEnoughFuel
