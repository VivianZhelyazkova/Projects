def sort_records(data):
    sorted_records = sorted(data, key=lambda item: (item['city'], item['name']))
    return sorted_records