# ---------------------------------find smallest-&-largest element------------------------------------------


numbers = [10, 5, 8, 20, 3]

# Initialize variables for the smallest and largest numbers
smallest = float('inf')  # Initialize to positive infinity
largest = float('-inf')  # Initialize to negative infinity

# Iterate through the array to find the smallest and largest numbers
for num in numbers:
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num


print("Smallest number:", smallest)
print("Largest number:", largest)

#------------------------------------------PROBLEM-2 -------------------------------------------------------

numbers = [10, 5, 8, -20, 3]

# Find the smallest and largest numbers using min() and max() functions
smallest = min(numbers)
largest = max(numbers)

print("Smallest number:", smallest)
print("Largest number:", largest)