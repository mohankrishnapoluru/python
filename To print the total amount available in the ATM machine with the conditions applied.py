def calculate_total_amount(denominations, notes):
    total_amount = 0
    for denomination, count in zip(denominations, notes):
        total_amount += denomination * count
    return total_amount

def main():
    # Available denominations
    denominations = [2000, 500, 200, 100]
    print("puneeth")    
    # Get denomination priority from the user
    print("Enter the priority of denominations (separated by space, e.g., 2000 500 200 100):")
    user_input = input().split()
    user_priority = [int(denomination) for denomination in user_input]
    
    
    
    # Get the number of notes for each denomination from the user
    notes = []
    for denomination in user_priority:
        count = int(input(f"Enter the number of {denomination} notes: "))
        notes.append(count)
    
    # Calculate and print the total amount
    total_amount = calculate_total_amount(user_priority, notes)
    print(f"Total amount available in the ATM: {total_amount}")

if __name__ == "__main__":
    main()

