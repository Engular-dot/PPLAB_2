def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiple(a,b):
    return a*b

def main():
    print("Simple calculator")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")
    print(f"5 * 2 = {multiple(5,2)}")

if __name__ == "__main__":
    main()
