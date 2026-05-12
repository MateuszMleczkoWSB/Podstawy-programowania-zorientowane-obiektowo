# Exercise 1: reminder of the basics of programming

# Simple two-number calculator
def calc():
    num1 = float(input("Enter first num: "))
    num2 = float(input("Enter second num: "))
    operation = input("Enter operation number: ('+' - plus; '-' - minus'; '*' - multiply; '/' - divide) ")

    if operation == '+':
        result = num1 + num2
        print(f"Result: {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"Result: {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"Result: {result}")
    elif operation == '/':
        if num2 == 0:
            print("You can't divide by zero")
            return
        else:
            result = num1 / num2
            print(f"Result: {result}")
    else:
        print("Wrong operation number")


# Temperature converter (Celsius --> Fahrenheit)
def tempConverter():
    operation = input("Enter operation: ('c' - If you want to convert Celsius to Fahrenheit; 'f' - If you want to convert Fahrenheit to Celsius): ")
    temp = float(input("Enter temperature to convert: "))

    if operation == 'c':
        print("Celsius --> Fahrenheit")
        result = (temp * 1.8) + 32
        print(f"{temp}℃ = {result}℉")
    elif operation == 'f':
        print("Fahrenheit --> Celsius")
        result = (temp - 32) / 1.8
        print(f"{temp}℉ = {result}℃")
    else:
        print("Entered wrong operation (set 'c' or 'f')")
