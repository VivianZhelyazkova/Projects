from store import Store, MarketStall
from supplier import Supplier
from trader import Trader


class CommercialChain(Trader):

    def __init__(self, name: str, address: str, capital: float, suppliers: list[Supplier], stores: list[Store]):
        if len(suppliers) > 15:
            raise Exception("Too many suppliers!")
        if len(stores) > 10:
            raise Exception("Too many stores!")
        for store in stores:
            if type(store) is MarketStall:
                raise Exception("Commercial chain traders cannot have market stalls!")
        super().__init__(name, address, capital, stores, suppliers)
