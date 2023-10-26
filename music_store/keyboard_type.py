from instrument import Instrument


class KeyboardInstrument(Instrument):

    def __init__(self, name: str, price: float, quantity: int, instrument_type: str):
        super().__init__(name, price, quantity)
        self.instrument_type = instrument_type
