# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract two numbers
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide two numbers
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."

# Main calculator logic
print("Welcome to the Simple Calculator!")
print("Select an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

try:
    choice = int(input("Enter the number of your choice (1/2/3/4):\n"))
    if choice in [1, 2, 3, 4]:
        num1 = float(input("Enter the first number:\n"))
        num2 = float(input("Enter the second number:\n"))

        if choice == 1:
            result = add(num1, num2)
            operation = "Addition"
        elif choice == 2:
            result = subtract(num1, num2)
            operation = "Subtraction"
        elif choice == 3:
            result = multiply(num1, num2)
            operation = "Multiplication"
        elif choice == 4:
            result = divide(num1, num2)
            operation = "Division"

        print(f"The result of {operation} is: {result}")
    else:
        print("Invalid choice! Please select a valid option.")
except ValueError:
    print("Error! Please enter valid numbers.")
