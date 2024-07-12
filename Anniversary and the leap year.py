def is_leap_year(year):
    # Check if the year is a leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def find_anniversary(year):
    if is_leap_year(year):
        print("Leap year")
        next_anniversary = year + 1
        print(f"The next anniversary is: {next_anniversary}")
    else:
        print("Not a leap year")
        previous_anniversary = year - 1
        print(f"The previous anniversary is: {previous_anniversary}")

# Sample input
anniversary_year = 2024
find_anniversary(anniversary_year)
print("puneeth")
# You can replace 2024 with any other year to test the function
