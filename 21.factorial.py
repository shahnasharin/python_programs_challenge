#---------------------------------------print the factorial of a number---------------------------------------

# Function to calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Input: Get the number for which you want to calculate the factorial
num = int(input("Enter a number: "))

# Check if the number is negative
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(num)
    print(f"The factorial of {num} is {result}")


#---------------------------------using for loop----------------------------------------------------

num = int(input("Enter a number: "))

# Check if the number is negative
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    # Initialize the factorial to 1
    factorial = 1

    # Calculate the factorial using a for loop
    for i in range(1, num + 1):
        factorial *= i

    print(f"The factorial of {num} is {factorial}")
