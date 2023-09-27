from io_util import write_to_file
from sort_util import sort_records
records = []
NUMBER_OF_ENTRIES = 2

for i in range(NUMBER_OF_ENTRIES):
    name = input("Enter your name:\n")
    city = input("Enter your city:\n")
    phone = input("Enter your phone:\n")
    person = {
        "city": city,
        "name": name,
        "phone": phone
    }
    records.append(person)

sorted_records = sort_records(records)
for record in sorted_records:
    print(f"{record['city']} {record['name']} {record['phone']}")

write_to_file(sorted_records)



