#-----------------------------count & sum of duplicate numbers---------------------------------------------

input_numbers = input("Enter a list of numbers separated by spaces: ")

numbers = [int(num) for num in input_numbers.split()]

duplicate_count = len(numbers) - len(set(numbers))  # Total count minus the count of unique numbers
sum_duplicates = sum([num for num in numbers if numbers.count(num) > 1])  # Sum of duplicates

print("Count of duplicate numbers:", duplicate_count)
print("Sum of duplicate numbers:", sum_duplicates)
