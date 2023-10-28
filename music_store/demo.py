from cash_register import CashRegister
from electronic_instrument import ElectronicInstrument
from keyboard_instrument import KeyboardInstrument
from percussion_instrument import PercussionInstrument
from string_instrument import StringInstrument
from woodwind_instrument import WoodwindInstrument
from store import Store
from instrument import Instrument, InstrumentType
from shop_statistics_util import *

guitar = StringInstrument("Guitar", 2500.00, 4, InstrumentType.STRING)
violin = StringInstrument("Violin", 500.00, 13, InstrumentType.STRING)
drum = PercussionInstrument("Drum", 3100.00, 2, InstrumentType.PERCUSSION)
tambourine = PercussionInstrument("Tambourine", 100.00, 23, InstrumentType.PERCUSSION)
synthesizer = ElectronicInstrument("Synthesizer", 800.00, 9, InstrumentType.ELECTRONIC)
oscillator = ElectronicInstrument("Oscillator", 300.00, 7, InstrumentType.ELECTRONIC)
piano = KeyboardInstrument("Piano", 12000.00, 3, InstrumentType.KEYBOARD)
organ = KeyboardInstrument("Organ", 52000.00, 1, InstrumentType.KEYBOARD)
saxophone = WoodwindInstrument("Saxophone", 1200.00, 12, InstrumentType.WOODWIND)
flute = WoodwindInstrument("Flute", 220.00, 42, InstrumentType.WOODWIND)

instruments: list[Instrument] = [guitar, violin, drum, tambourine, synthesizer, oscillator, piano, organ, saxophone,
                                 flute]
music_shop = Store(instruments, CashRegister(0))

music_shop.sell("Drums", 2)
music_shop.sell("Drums", 6)
music_shop.sell("Tambourine", 12)
music_shop.sell("Tambourine", 3)
music_shop.sell("Organ", 1)
music_shop.sell("Piano", 3)

music_shop.add_instruments("Drum", 3)
music_shop.add_instruments("Drum", 43535)

# sold_items_sorted_by_count(music_shop.sold_instruments)
# total_money_earned_from_sold_instruments(music_shop.sold_instruments)
# get_top_selling_instrument(music_shop.sold_instruments)
# get_least_selling_instrument(music_shop.sold_instruments, music_shop.instruments)
# top_selling_instrument_type_by_count(music_shop.sold_instruments)
# top_selling_instrument_type_by_price(music_shop.sold_instruments)
