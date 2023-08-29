#---------------------------------sum of unique numbers-------------------------------------------------------



input_numbers = input("Enter a list of numbers separated by spaces: ")

# Split the input string into a list of numbers and convert them to integers
numbers = [int(num) for num in input_numbers.split()]

# Calculate the count of unique numbers and their sum
unique_numbers = set(numbers)  # Convert the list to a set to remove duplicates
count_unique = len(unique_numbers)  # Count the unique numbers
sum_unique = sum(unique_numbers)  # Calculate the sum of unique numbers

print("Count of unique numbers:", count_unique)
print("Sum of unique numbers:", sum_unique)



#------------------------------with function-----------------------------------------------------------

def count_unique_and_sum(numbers):
    unique_numbers = set(numbers)
    count_unique = len(unique_numbers)
    sum_unique = sum(unique_numbers)
    return count_unique, sum_unique

input_numbers = input("Enter a list of numbers separated by spaces: ")

numbers = [int(num) for num in input_numbers.split()]

count, total_sum = count_unique_and_sum(numbers)

print("Count of unique numbers:", count)
print("Sum of unique numbers:", total_sum)

