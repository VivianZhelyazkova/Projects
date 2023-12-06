from supplier import RetailSupp
from trader import Trader


class Travelling(Trader):

    def __init__(self, name: str, address: str, capital: float, suppliers: list[RetailSupp]):
        super().__init__(name, address, capital, [], suppliers)



