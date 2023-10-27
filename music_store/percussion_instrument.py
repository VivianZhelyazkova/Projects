from instrument import Instrument, InstrumentType


class PercussionInstrument(Instrument):

    def __init__(self, name: str, price: float, quantity: int, instrument_type: InstrumentType):
        super().__init__(name, price, quantity)
        self.instrument_type = instrument_type
