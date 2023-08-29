# -----------------------------------------delete unique numbers from list-----------------------------

numbers = [1, 2, 2, 3, 4, 4, 5]

to_remove = []

# Iterate through the array and identify unique numbers
for num in numbers:
    if numbers.count(num) == 1:
        to_remove.append(num)

# Remove the identified unique numbers from the original array
for num in to_remove:
    numbers.remove(num)

print("Array with unique numbers removed:", numbers)




