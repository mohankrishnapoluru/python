print("puneeth")
def fibonacci(n):
    # Check if n is less than or equal to 0
    if n <= 0:
        return "Invalid input. Please enter a positive integer greater than zero."
    
    # Initialize the first two Fibonacci numbers
    fib_0, fib_1 = 0, 1
    
    # Calculate Fibonacci numbers iteratively
    for _ in range(2, n + 1):
        fib_next = fib_0 + fib_1
        fib_0 = fib_1
        fib_1 = fib_next
    
    return fib_1

def main():
    # Get input from the user
    try:
        n = int(input("Enter the value of N to find the Nth Fibonacci number: "))
        
        # Call the fibonacci function to find the Nth Fibonacci number
        result = fibonacci(n)
        
        # Print the result
        print(f"The {n}th Fibonacci number is: {result}")
    
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
