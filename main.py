num1 = float(input("Enter first number: "))
operation = input("Enter an operation (+, -, *, /): ")
num2 = float(input("Enter second number: "))

try:
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2 if num2 != 0 else "Error: Division by zero"
    else:
        raise ValueError("Error: Invalid operation")

    print(f"Result: {result}")

except ValueError as e:
    print(e)
