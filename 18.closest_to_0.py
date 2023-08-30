# -------------------------------------- find closest number to '0' -----------------------------------------


numbers = [10, -5, 8, -20, 3]

closest_number = numbers[0]  # Initialize with the first number
closest_absolute = abs(numbers[0])

# Iterate through the list to find the closest number to zero
for num in numbers:
    absolute_value = abs(num)
    if absolute_value < closest_absolute:
        closest_number = num
        closest_absolute = absolute_value

print("Closest number to zero:", closest_number)
