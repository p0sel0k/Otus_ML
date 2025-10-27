from homework_05.base import Vehicle
from homework_05.exceptions import CargoOverload


class Plane(Vehicle):
    
    def __init__(self, weight=2000, fuel=20_000, fuel_consumption=2.25, max_cargo: float = 23_000):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo: float = 0
        self.max_cargo = max_cargo
    

    def load_cargo(self, cargo: float):
        """Add cargo to the plain if it possible"""
        planned_cargo = self.cargo + cargo
        if planned_cargo > self.max_cargo:
            raise CargoOverload
        
        self.cargo = planned_cargo


    def remove_all_cargo(self) -> float:
        """Removes all cargo from the plane and returns its value"""
        all_cargo = self.cargo
        self.cargo = 0

        return all_cargo