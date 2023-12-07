from store import Store, MarketStall, PushCart
from supplier import RetailSupp
from trader import Trader


class Sole(Trader):

    def __init__(self, name: str, address: str, capital: float, suppliers: list[RetailSupp], stores: list[Store]):
        if len(suppliers) > 5:
            raise Exception("Too many suppliers!")
        for supplier in suppliers:
            if type(supplier) is not RetailSupp:
                raise Exception("The sole trader only operates with retail suppliers!")
        if len(stores) > 1:
            raise Exception("Too many stores")
        if type(stores[0]) not in [MarketStall, PushCart]:
            raise Exception("The sole trader can only have a market stall or a push cart!")
        super().__init__(name, address, capital, stores, suppliers)
