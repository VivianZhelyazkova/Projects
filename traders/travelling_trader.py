from supplier import RetailSupp
from trader import Trader


class Travelling(Trader):

    def __init__(self, name: str, address: str, capital: float, suppliers: list[RetailSupp]):
        if len(suppliers) > 1:
            raise Exception("Too many suppliers")
        if type(suppliers[0]) is not RetailSupp:
            raise Exception("The sole trader only operates with retail suppliers")
        super().__init__(name, address, capital, [], suppliers)




