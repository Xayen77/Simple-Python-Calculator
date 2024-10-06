import math

print("******************SIMPLE PYTHON CALCULATOR BY VISHALL**************************")
print("Available operations to perform are listed below:")
print("1. ADDITION")
print("2. SUBTRACTION")
print("3. MULTIPLICATION")
print("4. DIVISION")
print("5. SQUARE ROOT")
print("6. RAISE TO POWER")

operation = input("Choose your preferred operation (1-6): ")

# Convert the input into a number where necessary
if operation == "1":  # Addition
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    answer = num1 + num2
    print(f"The result is {answer}")
    
elif operation == "2":  # Subtraction
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    answer = num1 - num2
    print(f"The result is {answer}")
    
elif operation == "3":  # Multiplication
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    answer = num1 * num2
    print(f"The result is {answer}")
    
elif operation == "4":  # Division
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if num2 != 0:
        answer = num1 / num2
        print(f"The result is {answer}")
    else:
        print("Error! Division by zero is not allowed.")
    
elif operation == "5":  # Square Root
    num1 = float(input("Enter number: "))
    if num1 >= 0:
        answer = math.sqrt(num1)
        print(f"The result is {answer}")
    else:
        print("Error! Cannot take the square root of a negative number.")
    
elif operation == "6":  # Raise to Power
    num1 = float(input("Enter base number: "))
    num2 = float(input("Enter exponent: "))
    answer = math.pow(num1, num2)
    print(f"The result is {answer}")
    
else: 
    print("Invalid entry. Please try again.")
