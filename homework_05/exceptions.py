class LowFuelError(Exception):
    """There is not enough fuel to start or continue movement."""
    pass


class NotEnoughFuel(Exception):
    """Attempting to spend more fuel than the vehicle has."""
    pass


class CargoOverload(Exception):
    """Loading cargo exceeds the vehicle’s capacity."""
    pass
