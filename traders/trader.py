from supplier import Supplier, WholesaleSupp
from store import Store
from product import Product


class Trader:

    def __init__(self, name: str, address: str, capital: float, stores: list[Store], suppliers: list[Supplier]):
        self.name = name
        self.address = address
        self.capital = capital
        self.stores = stores
        self.suppliers = suppliers

    def order(self, products: list[Product], supplier: Supplier):
        discount = supplier.discount
        total_amount = 0
        for product in products:
            total_amount += product.price
        final_sum = total_amount * discount
        if total_amount > self.capital / 2:
            print("Total amount exceeds limit")
        else:
            self.capital -= final_sum

