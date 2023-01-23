"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload

class Plane(Vehicle):
    cargo = 0

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self,cargo_weight):
        if self.max_cargo < cargo_weight + self.cargo:
            print("overload")
            raise CargoOverload
        else:
            self.cargo = self.cargo + cargo_weight

    def remove_all_cargo(self):
        cargo_return = self.cargo
        self.cargo=0
        return cargo_return

# airbus = Plane(weight=1500, fuel=5.5, fuel_consumption=5.5,max_cargo=300)
# airbus.load_cargo(200)
# print(airbus.cargo)
# airbus.load_cargo(40)
# print(airbus.cargo)
# print(airbus.remove_all_cargo())
