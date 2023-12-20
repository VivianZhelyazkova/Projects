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
        self.profit = 0

    def order(self, products: list[Product], supplier: Supplier, store: Store):
        discount = supplier.discount
        total_amount = 0
        for product in products:
            total_amount += product.price
        final_sum = total_amount * discount
        if total_amount > self.capital / 2:
            print("Total amount exceeds limit")
        else:
            self.capital -= final_sum
            store.add_products(products)
            print("Ordered products:")
            products = sorted(products, key=lambda x: x.price)
            for product in products:
                print(f"Name: {product.name}; Price: {product.price}")

    def collect(self, store: Store):
        profit = store.sell_products()
        self.profit += profit
        print(f"Profit made: {profit:.2f}")
        available_products = sorted(store.available_products, key=lambda x: x.price)
        print(f"Available products:")
        for product in available_products:
            print(f"Name: {product.name}; Price: {product.price}")

    def pay_taxes(self, store: Store):
        if self.capital >= store.taxes:
            self.capital -= store.taxes
        elif self.profit >= store.taxes:
            self.profit -= store.taxes
        else:
            raise Exception("Bankrupt!")
        print(f"Paid taxes for store on {store.address}: {store.taxes}")



