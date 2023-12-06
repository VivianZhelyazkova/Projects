from abc import ABC


class Store(ABC):

    def __int__(self, address: str, working_hours: str, area: float, taxes: float):
        self.address = address
        self.working_hours = working_hours
        self.area = area
        self.taxes = taxes


class MarketStall(Store):

    def __init__(self, address: str, working_hours: str, area: float):
        super().__init__(address, working_hours, area, 50)


class MarketStall(Store):

    def __init__(self, address: str, working_hours: str, area: float):
        super().__init__(address, working_hours, area, 50)


class MarketStall(Store):

    def __init__(self, address: str, working_hours: str, area: float):
        super().__init__(address, working_hours, area, 50)
