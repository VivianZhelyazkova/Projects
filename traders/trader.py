from supplier import Supplier
from store import Store


class Trader:

    def __init__(self, name: str, address: str, capital: float, stores: list[Store], suppliers: list[Supplier]):
        self.name = name
        self.address = address
        self.capital = capital
        self.stores = stores
        self.suppliers = suppliers


    def order(self, products:list, supplier:Supplier):