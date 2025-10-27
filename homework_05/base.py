from abc import ABC
from homework_05.exceptions import LowFuelError, NotEnoughFuel

class Vehicle(ABC):

    def __init__(self, weight:float = 100.0, fuel: float = 50.0, fuel_consumption: float = 5.0):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):
        """Starts the vehicle if it has fuel."""

        if self.started:
            return
        
        if self.fuel < 0:
            raise LowFuelError
        
        self.started = True

    def move(self, distance: float):
        """Moves the vehicle the given distance if enough fuel is available."""

        fuel_to_move = distance * self.fuel_consumption
        if fuel_to_move < self.fuel:
            raise NotEnoughFuel
        
        self.fuel -= fuel_to_move
