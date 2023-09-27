from io_util import read_from_file, write_to_file
from sort_util import sort_records

records = read_from_file()
name = input("What is your name?\n")
name_found = False
# We are presuming that all names are unique
for record in records:
    if record["name"] == name:
        name_found = True
if not name_found:
    print("Your name is not in the list.")
    exit()
command = input("Did you change your city? Y/N\n")
if command == "Y":
    new_city = input("What is your new city?\n")
    for record in records:
        if record["name"] == name:
            record["city"] = new_city
            print("Your city has been updated.")

command = input("Did you change your phone number? Y/N\n")
if command == "Y":
    new_phone = input("What is your new phone number?\n")
    for record in records:
        if record["name"] == name:
            record["phone"] = new_phone
            print("Your phone number has been updated.")

sorted_records = sort_records(records)
write_to_file(sorted_records)



