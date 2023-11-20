import time
from colorama import Back, Fore

first_line = "Wake up, Neo..."
second_line = "The Matrix has you..."
third_line = "Follow the white rabbit."


def print_line(line):
    for char in line:
        # print(char, end="", flush=True)
        print(Back.BLACK + Fore.GREEN + char, end="", flush=True)
        time.sleep(0.21)
    print()
    time.sleep(1)


print_line(first_line)
print_line(second_line)
print_line(third_line)
