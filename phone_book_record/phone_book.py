from io_util import write_to_file
from sort_util import sort_records
records = []
NUMBER_OF_ENTRIES = 10

for i in range(NUMBER_OF_ENTRIES):
    name = input("Enter your name:\n")
    city = input("Enter your city:\n")
    phone = input("Enter your phone:\n")
    person = {
        "city": city,
        "name": name,
        "phone": phone
    }
    counter = 0
    for record in records:
        record_name = record["name"].split("_")[0]
        if name == record_name:
            counter += 1
    if counter > 0:
        name += '_' + str(counter)
        person["name"] = name


    records.append(person)

sorted_records = sort_records(records)
for record in sorted_records:
    print(f"{record['city']} {record['name']} {record['phone']}")

write_to_file(sorted_records)



