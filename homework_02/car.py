"""
создайте класс `Car`, наследник `Vehicle`
"""

from homework_02.base import Vehicle
from homework_02.engine import Engine


class Car(Vehicle):
    engine = None
    def set_engine(self, engine):
        self.engine = engine

# focus2 = Car(weight=1500, fuel=5.5, fuel_consumption=5.5)
#
# volume = 1.6
# pistons = 4
# engine = Engine(volume=volume, pistons=pistons)
#
# focus2.set_engine(engine)
# print(focus2.engine.pistons)
# print(focus2.engine.volume)