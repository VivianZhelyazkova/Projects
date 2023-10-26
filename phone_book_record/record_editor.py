from io_util import read_from_file, write_to_file
from sort_util import sort_records
user_record = None
records = read_from_file()
phone_number = input("What is your telephone number?\n")
# We are identifying users by telephone numbers, since it is the only unique information
for record in records:
    if record["phone"] == phone_number:
        print(f"Hello {record['name']}!")
        user_record = record
if not user_record:
    print("Your phone number is not in the list.")
    exit()
command = input("Did you change your city? Y/N\n")
if command == "Y":
    new_city = input("What is your new city?\n")
    user_record["city"] = new_city
    print("Your city has been updated.")

command = input("Did you change your phone number? Y/N\n")
if command == "Y":
    new_phone = input("What is your new phone number?\n")
    user_record["phone"] = new_phone
    print("Your phone number has been updated.")

sorted_records = sort_records(records)
write_to_file(sorted_records)
