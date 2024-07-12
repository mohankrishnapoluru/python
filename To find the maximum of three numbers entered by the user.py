def find_maximum(a,b, c):
    # Using Python's built-in max function to find the maximum
    return max(a, b, c)

def main():
    print("puneeth")
    # Get input from the user
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        c = float(input("Enter the third number: "))
        
        # Find the maximum number among the three
        maximum_number = find_maximum(a, b, c)
        
        # Print the result
        print(f"The maximum of the three numbers {a}, {b}, {c} is: {maximum_number}")
    
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
