import copy
from instrument import Instrument
from cash_register import CashRegister
from shop_statistics_util import *


class Store:

    def __init__(self, instruments: list[Instrument],cash_register: CashRegister):
        self.instruments = instruments
        self.sold_instruments: list[Instrument] = []
        self.cash_register = cash_register

    def sell(self, name: str, count: int):
        for instrument in self.instruments:
            if instrument.name == name:
                if count <= instrument.quantity:
                    instrument.quantity -= count
                    self.cash_register.add_money(count * instrument.price)
                    print(f"{count} {name} sold!")
                    sold_item_found = False
                    for sold_item in self.sold_instruments:
                        if sold_item.name == name:
                            sold_item.quantity += count
                            sold_item_found = True
                    if not sold_item_found:
                        instrument_copy = copy.deepcopy(instrument)
                        instrument_copy.quantity = count
                        self.sold_instruments.append(instrument_copy)
                else:
                    print(f"Instrument not in stock")

    def add_instruments(self, name: str, count: int):
        for instrument in self.instruments:
            if name == instrument.name:
                instrument.quantity += count

    def print_catalog(self, reverse: bool = False):
        self.sort_by(lambda item: item.instrument_type, "type")
        self.sort_by(lambda item: item.name, "name")
        self.sort_by(lambda item: item.price, "price", reverse)
        in_stock = list(filter(lambda item: item.quantity > 0, self.instruments))
        print(f"***In stock***")
        for instrument in in_stock:
            print(instrument)

    def sort_by(self, key, sorted_by: str, reverse=False):
        sorted_list = self.instruments.copy()
        sorted_list.sort(key=key, reverse=reverse)
        print(f"***Sorted by {sorted_by}***")
        for instrument in sorted_list:
            print(instrument)
