def is_prime(n):
    # Check if n is less than 2
    if n < 2:
        return False
    # Check if n is 2 or 3
    if n in (2, 3):
        return True
    # Eliminate even numbers and numbers divisible by 3
    if n % 2 == 0 or n % 3 == 0:
        return False
    # Check for factors up to the square root of n
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def print_non_primes(A, B):
    for num in range(A, B + 1):
        if not is_prime(num):
            print(num)

# Define the range
A = 10
B = 30
print_non_primes(A, B)
print("puneeth")
      
