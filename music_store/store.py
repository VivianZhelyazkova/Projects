from Practice.music_store.string_type import StringInstrument
from instrument import Instrument
from cash_register import CashRegister


class Store:

    def __init__(self, instruments: list[Instrument]):
        self.instruments = instruments

    def sell(self, name: str, count: int):
        for instrument in self.instruments:
            if instrument.name == name:
                if count <= instrument.quantity:
                    instrument.quantity -= count
                    CashRegister.add_money(count * instrument.price)
                else:
                    print(f"Instrument not in stock")

    def add_instruments(self, name: str, count: int):
        for instrument in self.instruments:
            if name == instrument.name:
                instrument.quantity += count

    def catalog(self, reverse: bool):
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
