import copy

from Practice.music_store.instrument import Instrument


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
    sorted_by_quantity.sort(key=lambda item: item.quantity)
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
        if instrument not in sold_instruments:
            instrument_copy = copy.deepcopy(instrument)
            instrument_copy.quantity = 0
            sorted_by_quantity.append(instrument_copy)
    sorted_by_quantity.sort(key=lambda item: item.quantity, reverse=True)
    least_selling_item = sorted_by_quantity[0]
    least_selling_list.append(least_selling_item)
    for index in range(1, len(sorted_by_quantity)):
        if sorted_by_quantity[index].quantity == least_selling_item.quantity:
            least_selling_list.append(sorted_by_quantity[index])
    print(f"***Least selling instruments***")
    for instrument in least_selling_list:
        print(instrument)
