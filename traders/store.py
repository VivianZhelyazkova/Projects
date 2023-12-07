from abc import ABC
import random

from product import Product


class Store(ABC):
    MARGIN = 1.30

    def __int__(self, address: str, working_hours: str, area: float, taxes: float):
        self.address = address
        self.working_hours = working_hours
        self.area = area
        self.taxes = taxes
        self.available_products: list[Product] = []

    def add_products(self, products: list[Product]):
        self.available_products += products

    def sell_products(self):
        number_of_products_to_sell = random.randint(1, len(self.available_products) - 1)
        profit = 0
        for index in range(number_of_products_to_sell):
            profit += self.available_products[index].price
        self.available_products = self.available_products[number_of_products_to_sell:]
        final_profit = profit * Store.MARGIN
        return final_profit


class MarketStall(Store):

    def __init__(self, address: str, working_hours: str):
        area = random.randint(2, 10)
        super().__init__(address, working_hours, area, 50)


class MallShop(Store):

    def __init__(self, address: str, working_hours: str):
        area = random.randint(10, 100)
        super().__init__(address, working_hours, area, 150)


class PushCart(Store):

    def __init__(self, address: str, working_hours: str):
        area = random.randint(4, 6)
        super().__init__(address, working_hours, area, 50)
