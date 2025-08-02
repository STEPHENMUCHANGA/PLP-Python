# Basic Calculator Program
# This program takes two numbers and an arithmetic operation from the user
# and performs the corresponding calculation.
def calculator():
    print("=== Basic Calculator ===")

    # Prompt user for the first number
    try:
        num1 = float(input("Enter the first number: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    # Prompt user for the second number
    try:
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    # Prompt user for the operation
    operation = input("Enter an operation (+, -, *, /): ").strip()
    
    # Perform the operation and display the result
    if operation == '+':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == '/':
        # Handle division by zero
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
    else:
        print("Invalid operation. Please enter one of +, -, *, /.")

       
