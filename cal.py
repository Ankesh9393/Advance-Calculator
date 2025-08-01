import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def modulus(x, y):
    return x % y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Error! Cannot calculate square root of a negative number."
    return math.sqrt(x)

print("\n--- Advanced Calculator ---")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")
print("6. Power")
print("7. Square Root")
print("8. Exit")

while True:
    choice = input("\nEnter choice (1-8): ")

    if choice == '8':
        print("Exiting calculator. Goodbye!")
        break

    if choice in ('1', '2', '3', '4', '5', '6'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"Result: {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Result: {divide(num1, num2)}")
        elif choice == '5':
            print(f"Result: {modulus(num1, num2)}")
        elif choice == '6':
            print(f"Result: {power(num1, num2)}")

    elif choice == '7':
        num = float(input("Enter number: "))
        print(f"Result: {square_root(num)}")
    else:
        print("Invalid input! Please select a valid option.")
