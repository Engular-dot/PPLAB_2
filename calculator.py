def add(a, b):
    return a + b


def substract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def main():
    print("Simple calculator")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 3 = {substract(5, 3)}")
    print(f"2 * 3 = {multiply(2, 3)}")
    print(f"6 + 3 = {divide(6, 3)}")


if __name__ == "__main__":
    main()
