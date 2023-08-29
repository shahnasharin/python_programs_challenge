#--find sum of even numbers from a list??-----------PROBLEM-1------------------------------------

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_sum = 0

for num in numbers:
    if num % 2 == 0:
        even_sum += num

print("Sum of even numbers:", even_sum)


#------------------------------------------PROBLEM-2------------------------------------------------

input_numbers = input("Enter a list of numbers separated by spaces: ")

# Split the input string into a list of numbers
numbers = [int(num) for num in input_numbers.split()]

even_sum = 0

for num in numbers:
    if num % 2 == 0:
        even_sum += num
        
print("Sum of even numbers:", even_sum)
