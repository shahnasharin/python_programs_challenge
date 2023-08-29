# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0: 
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = [num for num in numbers if is_prime(num)]
print("Prime numbers in the array:", prime_numbers)

