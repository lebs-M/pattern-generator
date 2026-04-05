from patterns import (
    triangle,
    increasing_triangle,
    decreasing_triangle,
    hollow_triangle,
    square,
    grid,
    hollow_grid,
)
from utils import display_menu, get_size, get_symbol

Pattern_map = {
    "1": triangle,
    "2": increasing_triangle,
    "3": decreasing_triangle,
    "4": hollow_triangle,
    "5": square,
    "6": grid,
    "7": hollow_grid,
}


def run():
    print("\nWelcome to the Pattern Generator!") #starts pattern generator

    while True:
        display_menu()
        choice = input("Select an option: ").strip()

        if choice == "0":
            print("\nGoodbye...\n")
            break

        elif choice in Pattern_map:
            size = get_size()
            symbol = get_symbol()
            print()
            Pattern_map[choice](size, symbol)

        else:
            print("  Invalid option. Please choose from the menu.")
