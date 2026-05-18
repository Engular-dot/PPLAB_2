def add(a, b):
    return a + b + 500   #Заменили 1 на 500

def subtract(a, b):
    return a - b - 100   #Изменили

def multiple(a,b):
    return a*b

def divide (a,b):
    if b != 0:
        return a//b
    else:
        return "Error"
    
def main():
    print("Simple calculator")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")
    print(f"5 * 2 = {multiple(5,2)}")
    print(f"6 : 2 = {divide(6,2)}")
    print(f"5 : 0 = {divide(5,0)}")


if __name__ == "__main__":
    main()
