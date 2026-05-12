# Exercise 1: reminder of the basics of programming

# Starting method
def start():
    while True:
        program = int(input("Select program (1: Simple two-number calculator; 2: Temperature converter (Celsius --> Fahrenheit); 3: Student's grades average): "))

        if program == 1:
            calc()
        elif program == 2:
            tempConverter()
        elif program == 3:
            gradesAverage()
        else:
            start()

# Simple two-number calculator
def calc():
    print("Simple two-number calculator")
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
        print("Wrong operation selected")
        calc()


# Temperature converter (Celsius --> Fahrenheit)
def tempConverter():
    print("Temperature converter (Celsius --> Fahrenheit)")
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
        tempConverter()


# Student's grades average
def gradesAverage():
    print("Student's grades average")
    numOfGrades = int(input('Enter number of grades: '))
    sum = 0

    for i in range(numOfGrades):
        while True:
            grade = int(input('Enter grade (1-6): '))

            if grade < 1 or grade > 6:
                continue
            else:
                sum += grade
                break

    average = sum / numOfGrades
    print(f"Grades average: {average}")

    if average >= 3:
        print('Student passed')
    else:
        print('Student failed')


start()