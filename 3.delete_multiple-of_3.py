# ----------------------------------------------problem-1:-----------------------------------

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Create a new list without multiples of 3
filtered_numbers = [num for num in numbers if num % 3 != 0]

print("Original List:", numbers)
print("List without multiples of 3:", filtered_numbers)

# ----------------------------------------------problem-2:-----------------------------------

input_numbers = input("Enter a list of numbers separated by spaces: ")

# Split the input string into a list of numbers
numbers = [int(num) for num in input_numbers.split()]

# Create a new list without multiples of 3
filtered_numbers = [num for num in numbers if num % 3 != 0]

print("Original List:", numbers)
print("List without multiples of 3:", filtered_numbers)

