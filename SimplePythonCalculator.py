import math

print("******************SIMPLE PYTHON CALCULATOR BY VISHALL**************************")

print("Available operations to perform are listed below")
print("1. ADDITION")
print("2. SUBTRACTION")
print("3. MULTIPLICATION")
print("4. DIVISION")
print("5. SQUARE ROOT")
print("6. RAISE TO POWER")

operation = input("Choose your preferred operation (1-6): ")

if operation == "1": 
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    answer = num1 + num2 
    print("The final value is " + str(answer))
    
elif operation == "2": 
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    answer = num1 - num2 
    print("The final value is " + str(answer))
    
elif operation == "3": 
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    answer = num1 * num2 
    print("The final value is " + str(answer))
    
elif operation == "4": 
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    answer = num1 / num2 
    print("The final value is " + str(answer))
    
elif operation == "5": 
    num1 = float(input("Enter number: "))
    answer = math.sqrt(num1) 
    print("The result is " + str(answer))
    
elif operation == "6": 
    num1 = float(input("Enter number: "))
    exponent = float(input("Enter exponent: "))
    answer = math.pow(num1, exponent)
    print("The result is " + str(answer))
    
else: 
    print("Invalid entry. Please try again.")

# Keep the command prompt open
input("Press Enter to exit...")

