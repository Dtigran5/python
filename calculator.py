def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y != 0:
        return  x / y
    else:
        return "Cannot divide by zero"

operations = {'+': add, '-': subtract, '*': multiply, '/': divide}

def calculator(operator, x, y):
    if operator in operations:
        operation = operations[operator]
        result = operation(x, y)
        return result
    else:
        return "Invalid operator"

operator = input("Enter operator (+, -, *, /): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
result = calculator(operator, num1, num2)
print(f"Result: {result}")

