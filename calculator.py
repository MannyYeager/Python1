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
def square_root(x):
    if x < 0:
        return "Error! Cannot have square root of a negative number."
    return x ** 0.5
def power(x, y):
    return x ** y
def percentage(x, y):
    return (x / y) * 100
def reciprocal(x):
    if x == 0:
        return "Error! There cannot be division by zero."
    return 1 / x
def modulo(x, y):
    if y == 0:
        return "Error! There cannot be division by zero."
    return x % y
print("Welcome to your Calculator!")
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Square Root")
print("6. Power")
print("7. Percentage")
print("8. Reciprocal")
print("9. Modulo")
while True:
    choice = input("Enter choice (1/2/3/4/5/6/7/8/9): ")
    if choice in ['1', '2', '3', '4', '6', '7', '9']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: ")) 
        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        elif choice == '6':
            print(f"{num1} raised to the power of {num2} = {power(num1, num2)}")
        elif choice == '7':
            print(f"The percetage of {num1} and {num2} = {percentage(num1, num2)}")   
        elif choice == '9':
            print(f"The modulo of {num1} and {num2} = {modulo(num1, num2)}")  
    elif choice == '5':
        value1 = float(input("Enter your value: "))
        print(f"Square root of {value1} = {square_root(value1)}")   
    elif choice == '8':
        value1 = float(input("Enter your value: "))         
        print(f"The reciprocal of {value1} = {reciprocal(value1)}")   
       
        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break
    else:
        print("Invalid Input")