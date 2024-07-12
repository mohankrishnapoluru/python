print("puneeth")
# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    # Check if the denominator is zero
    if y == 0:
        return "Error: Division by zero!"
    else:
        return x / y

def main():
    print("Welcome to the Basic Calculator!")
    print("Operations available:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    while True:
        # Take input from the user
        choice = input("Enter choice (1/2/3/4): ")

        # Check if choice is one of the four options
        if choice in ('1', '2', '3', '4'):
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
            
            # Ask user if they want to perform another calculation
            another_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
            if another_calculation != 'yes':
                break
        else:
            print("Invalid input. Please enter a valid choice (1/2/3/4).")

    print("Thank you for using the Basic Calculator!")

if __name__ == "__main__":
    main()
