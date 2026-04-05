def get_size(label="Enter size"):
    while True: #prompt user for valid pattern size  (1-20)
        try:
            size = int(input(f"{label} (1-20): "))
            if 1 <= size <= 20:
                return size
            print("  Please enter a number between 1 and 20.")
        except ValueError:
            print("  Invalid input. Please enter a whole number.")


def get_symbol():
    symbol = input("Enter a symbol to use (default is *): ").strip() 
    return symbol[0] if symbol else "*"


def display_menu():
    print("\n" + "=" * 40)
    print("       PATTERN GENERATOR CLI")
    print("=" * 40)
    print("  1. Triangle")
    print("  2. Increasing Triangle")
    print("  3. Decreasing Triangle")
    print("  4. Hollow Triangle")
    print("  5. Square")
    print("  6. Grid")
    print("  7. Hollow Grid")
    print("  0. Exit")
    print("=" * 40)
