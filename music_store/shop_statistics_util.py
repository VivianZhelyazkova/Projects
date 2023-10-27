import copy

from Practice.music_store.instrument import Instrument, InstrumentType


def sold_items_sorted_by_count(sold_instruments: list[Instrument]):
    sorted_list = sold_instruments.copy()
    sorted_list.sort(key=lambda item: item.quantity)
    print(f"***Sold instruments by count***")
    for instrument in sorted_list:
        print(instrument)


def total_money_earned_from_sold_instruments(sold_instruments: list[Instrument]):
    total_money = 0
    for instrument in sold_instruments:
        total_money += instrument.price * instrument.quantity
    print(f"Total money earned: {total_money:.2f}")


def get_top_selling_instrument(sold_instruments: list[Instrument]):
    top_selling_list = []
    sorted_by_quantity = sold_instruments.copy()
    sorted_by_quantity.sort(key=lambda item: item.quantity, reverse=True)
    top_selling_item = sorted_by_quantity[0]
    top_selling_list.append(top_selling_item)
    for index in range(1, len(sorted_by_quantity)):
        if sorted_by_quantity[index].quantity == top_selling_item.quantity:
            top_selling_list.append(sorted_by_quantity[index])
    print(f"***Top selling instruments***")
    for instrument in top_selling_list:
        print(instrument)


def get_least_selling_instrument(sold_instruments: list[Instrument], instruments: list[Instrument]):
    least_selling_list = []
    sorted_by_quantity = sold_instruments.copy()
    for instrument in instruments:
        is_not_found = True
        for sold_instrument in sold_instruments:
            if instrument.name == sold_instrument.name:
                is_not_found = False
        if is_not_found:
            instrument_copy = copy.deepcopy(instrument)
            instrument_copy.quantity = 0
            sorted_by_quantity.append(instrument_copy)
    sorted_by_quantity.sort(key=lambda item: item.quantity)
    least_selling_item = sorted_by_quantity[0]
    least_selling_list.append(least_selling_item)
    for index in range(1, len(sorted_by_quantity)):
        if sorted_by_quantity[index].quantity == least_selling_item.quantity:
            least_selling_list.append(sorted_by_quantity[index])
    print(f"***Least selling instruments***")
    for instrument in least_selling_list:
        print(instrument)


def top_selling_instrument_type_by_count(sold_instruments: list[Instrument]):
    return top_selling_instrument_type_by(sold_instruments, True)


def top_selling_instrument_type_by_price(sold_instruments: list[Instrument]):
    return top_selling_instrument_type_by(sold_instruments, False)


def top_selling_instrument_type_by(sold_instruments: list[Instrument], by_count):
    sold_types = {
        InstrumentType.STRING: 0,
        InstrumentType.ELECTRONIC: 0,
        InstrumentType.KEYBOARD: 0,
        InstrumentType.PERCUSSION: 0,
        InstrumentType.WOODWIND: 0
    }

    for instrument in sold_instruments:
        value_to_add = instrument.quantity
        if not by_count:
            value_to_add = instrument.quantity * instrument.price
        sold_types[instrument.instrument_type] += value_to_add

    top_selling_type_key = max(sold_types, key=sold_types.get)
    top_selling_type_value = sold_types[top_selling_type_key]

    if by_count:
        print("***Top selling instrument type by count***")
        print(f"{str(top_selling_type_key.value).capitalize()} has been sold {top_selling_type_value} times.")
    else:
        print("***Top selling instrument type by price***")
        print(f"{str(top_selling_type_key.value).capitalize()} with profit of {top_selling_type_value:.2f}.")
