from Practice.music_store.cash_register import CashRegister
from Practice.music_store.electronic_instrument import ElectronicInstrument
from Practice.music_store.keyboard_instrument import KeyboardInstrument
from Practice.music_store.percussion_instrument import PercussionInstrument
from Practice.music_store.string_instrument import StringInstrument
from Practice.music_store.woodwind_instrument import WoodwindInstrument
from store import Store
from instrument import Instrument, InstrumentType

guitar = StringInstrument("Guitar", 2500.00, 4, InstrumentType.STRING)
violin = StringInstrument("Violin", 500.00, 13, InstrumentType.STRING)
drums = PercussionInstrument("Drums", 3100.00, 2, InstrumentType.PERCUSSION)
tambourine = PercussionInstrument("Tambourine", 100.00, 23, InstrumentType.PERCUSSION)
synthesizer = ElectronicInstrument("Synthesizer", 800.00, 9, InstrumentType.ELECTRONIC)
oscillator = ElectronicInstrument("Oscillator", 300.00, 7, InstrumentType.ELECTRONIC)
piano = KeyboardInstrument("Piano", 12000.00, 3, InstrumentType.KEYBOARD)
organ = KeyboardInstrument("Organ", 52000.00, 1, InstrumentType.KEYBOARD)
saxophone = WoodwindInstrument("Saxophone", 1200.00, 12, InstrumentType.WOODWIND)
flute = WoodwindInstrument("Flute", 220.00, 42, InstrumentType.WOODWIND)

instruments: list[Instrument] = [guitar, violin, drums, tambourine, synthesizer, oscillator, piano, organ, saxophone,
                                 flute]
music_shop = Store(instruments, CashRegister(0))

music_shop.sell("Drums", 2)
music_shop.sell("Drums", 2)
print(music_shop.cash_register.get_money())
music_shop.add_instruments("Drums", 3)
music_shop.print_catalog()
