def calculate (num1, num2, operation):
    if operation == "1":
        return num1 +num2
    elif operation == "2":
        return num1 - num2
    elif operation == "3":
        return num1 * num2
    elif operation == "4":
        return num1 / num2  if num2 != 0 else "Error: Division by zero"
    else:
        return "invalid operation"    
    
# Prompt
print("CALCULATOR")
num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
print("\n Choose the operation:")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
operation = input("Enter your choice(1/2/3/4):")
result = calculate(num1, num2, operation)
print("\n Result: ", result)
