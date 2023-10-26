class Instrument:

    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.instrument_type = None

    def __repr__(self):
        return f"Name: {self.name}; Price: {self.price}; Quantity: {self.quantity}; Type: {self.instrument_type}"
