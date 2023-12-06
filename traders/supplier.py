from abc import ABC


class Supplier(ABC):

    def __init__(self, name: str, address: str, working_hours: str):
        self.name = name
        self.address = address
        self.working_hours = working_hours


class WholesaleSupp(Supplier):

    def __init__(self, name: str, address: str, working_hours: str):
        super().__init__(name, address, working_hours)
        self.discount = 0.85


class RetailSupp(Supplier):

    def __init__(self, name: str, address: str, working_hours: str):
        super().__init__(name, address, working_hours)
        self.discount = 1
