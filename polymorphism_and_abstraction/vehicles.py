from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance: float) -> None:
        ...

    @abstractmethod
    def refuel(self, fuel: float) -> None:
        ...


class Car(Vehicle):
    CONDITIONER_CONSUMPTION = 0.9

    def drive(self, distance: float) -> None:
        total_fuel_consumption = (self.fuel_consumption + self.CONDITIONER_CONSUMPTION) * distance

        if self.fuel_quantity >= total_fuel_consumption:
            self.fuel_quantity -= total_fuel_consumption

    def refuel(self, fuel: float) -> None:
        self.fuel_quantity += fuel


class Truck(Vehicle):
    CONDITIONER_CONSUMPTION = 1.6
    LEAK_IN_TANK = 0.95

    def drive(self, distance: float) -> None:
        total_fuel_consumption = (self.fuel_consumption + self.CONDITIONER_CONSUMPTION) * distance

        if self.fuel_quantity >= total_fuel_consumption:
            self.fuel_quantity -= total_fuel_consumption

    def refuel(self, fuel: float) -> None:
        self.fuel_quantity += fuel * self.LEAK_IN_TANK






