#--------------------------------------delete duplicate elements--------------------------------------------

numbers = [1, 2, 2, 3, 4, 4, 5]

# Remove duplicates by converting the array to a set and then back to a list
unique_numbers = list(set(numbers))

print("Array with duplicates removed:", unique_numbers)


#------------------------------delete all duplicate elements-----------------------------------------------

numbers = [1, 2, 2, 3, 4, 4, 5]

unique_numbers = []

# Iterate through the array and add elements to unique_numbers if they are not duplicated
for num in numbers:
    if numbers.count(num) == 1:
        unique_numbers.append(num)

print("Unique elements:", unique_numbers)
