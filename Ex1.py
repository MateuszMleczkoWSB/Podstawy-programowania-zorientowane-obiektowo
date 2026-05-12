# Zadanie 1: przypomnienie podstaw programowania

# Prosty kalkulator dwóch liczb

def calc():
    num1 = float(input("Enter first num: "))
    num2 = float(input("Enter second num: "))
    operation = int(input("Enter operation number: (1: '+' - plus; 2: '-' - minus'; 3: '*' - multiply; 4: '/' - divide) "))

    if (operation == 1):
        result = num1 + num2
        print(f"Sum: {result}")
    elif (operation == 2):
        result = num1 - num2
        print(f"Result: {result}")
    elif (operation == 3):
        result = num1 * num2
        print(f"Result: {result}")
    elif (operation == 4):
        if (num2 == 0):
            print("You can't divide by zero")
            return
        else:
            result = num1 / num2
            print(f"Result: {result}")
    else:
        print("Wrong operation number")