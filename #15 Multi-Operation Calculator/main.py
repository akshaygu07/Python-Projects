def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
first = input("Enter first number: ")
second = input("Enter second number: ")
operation = input("Enter operation (+,-,*,/): ")
if operation == '+':
    print(add(int(first), int(second)))
if operation == '-':
    print(subtract(int(first), int(second)))
if operation == '*':
    print(multiply(int(first), int(second)))
if operation == '/':
    print(divide(int(first), int(second)))
