num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
operation = input("Enter a mathematical operation(+m -, *, /): ")
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
    result = num1 / num2
    print(f"{num1} / {num2} = {result}")
else:
    print("Invalid operation")