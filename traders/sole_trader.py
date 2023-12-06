from supplier import RetailSupp
from trader import Trader


class Sole(Trader):

    def __init__(self, name: str, address: str, capital: float, suppliers: list[RetailSupp], stores: list[Store]):
        super().__init__(name, address, capital, stores, suppliers)
