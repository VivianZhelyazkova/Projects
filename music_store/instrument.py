from enum import Enum


class InstrumentType(Enum):
    STRING = "string"
    ELECTRONIC = "electronic"
    KEYBOARD = "keyboard"
    PERCUSSION = "percussion"
    WOODWIND = "woodwind"
    NONE = None

    def __lt__(self, other):
        return str(self).split(".")[1] < str(other).split(".")[1]


class Instrument:

    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.instrument_type: InstrumentType = InstrumentType.NONE

    def __repr__(self):
        return f"Name: {self.name}; Price: {self.price}; Quantity: {self.quantity}; Type: {self.instrument_type.value}"