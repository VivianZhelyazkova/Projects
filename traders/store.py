from abc import ABC
import random


class Store(ABC):

    def __int__(self, address: str, working_hours: str, area: float, taxes: float):
        self.address = address
        self.working_hours = working_hours
        self.area = area
        self.taxes = taxes


class MarketStall(Store):

    def __init__(self, address: str, working_hours: str):
        area = random.randint(2, 10)
        super().__init__(address, working_hours, area, 50)


class MallShop(Store):

    def __init__(self, address: str, working_hours: str):
        area = random.randint(10, 100)
        super().__init__(address, working_hours, area, 150)


class PushCart(Store):

    def __init__(self, address: str, working_hours: str):
        area = random.randint(4, 6)
        super().__init__(address, working_hours, area, 50)
