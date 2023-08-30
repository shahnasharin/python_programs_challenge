# ------------------separate odd and even numbers in to separate array -------------------------------------


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

odd_numbers = []
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

print("Odd numbers:", odd_numbers)
print("Even numbers:", even_numbers)
