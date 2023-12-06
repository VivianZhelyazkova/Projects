from Practice.traders.store import Store
from supplier import RetailSupp
from trader import Trader


class Sole(Trader):

    def __init__(self, name: str, address: str, capital: float, suppliers: list[RetailSupp], stores: list[Store]):
        if len(suppliers) > 5:
            raise Exception("Too many suppliers")
        for supplier in suppliers:
            if type(supplier) is not RetailSupp:
                raise Exception("The sole trader only operates with retail suppliers")
        super().__init__(name, address, capital, stores, suppliers)
