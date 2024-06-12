from abc import ABC, abstractmethod
from math import log2


class Computer(ABC):

    PRICE_PER_RAM_BLOCK = 100

    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value: str):
        if value.strip() == "":
            raise ValueError("Manufacturer name cannot be empty.")
        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value: str):
        if value.strip() == "":
            raise ValueError("Model name cannot be empty.")
        self.__model = value

    @property
    @abstractmethod
    def get_processor(self):
        ...

    @property
    @abstractmethod
    def get_max_ram(self):
        ...

    @property
    @abstractmethod
    def get_type(self):
        ...

    @staticmethod
    def ram_possibilities(ram: int):
        result = log2(ram)
        return result.is_integer()

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.get_processor:
            raise ValueError(f"{processor} is not compatible with {self.get_type} {self.manufacturer} {self.model}!")

        if ram > self.get_max_ram or not self.ram_possibilities(ram):
            raise ValueError(f"{ram}GB RAM is not compatible with {self.get_type} {self.manufacturer} {self.model}!")

        self.set_parts(processor, ram)

        return f"Created {self.__repr__()} for {self.price}$."

    def set_parts(self, processor, ram):
        self.processor = processor
        self.ram = ram
        self.price += self.get_processor[processor]
        self.price += int(log2(ram)) * self.PRICE_PER_RAM_BLOCK

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"
