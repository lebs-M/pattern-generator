def triangle(size, symbol="*"):
    for i in range(1, size + 1): #triangle
        print(symbol * i)


def increasing_triangle(size, symbol="*"):
    for i in range(1, size + 1):
        spaces = " " * (size - i)
        print(spaces + symbol * (2 * i - 1))


def decreasing_triangle(size, symbol="*"):
    for i in range(size, 0, -1):
        spaces = " " * (size - i)
        print(spaces + symbol * (2 * i - 1))


def hollow_triangle(size, symbol="*"):
    for i in range(1, size + 1):
        if i == 1:
            print(symbol)
        elif i == size:
            print(symbol * size)
        else:
            print(symbol + " " * (i - 2) + symbol)


def square(size, symbol="*"):
    for _ in range(size):
        print(symbol * size)


def grid(size, symbol="*"):
    for i in range(size):
        row = ""
        for j in range(size):
            row += symbol if (i + j) % 2 == 0 else " "
        print(row)


def hollow_grid(size, symbol="*"):
    for i in range(size):
        if i == 0 or i == size - 1:
            print(symbol * size)
        else:
            print(symbol + " " * (size - 2) + symbol)
