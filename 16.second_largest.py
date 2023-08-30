#  ----------------------------------print second largest number -----------------------------------

numbers = [10, 5, 8, 20, 3]

numbers.sort(reverse=True)

if len(numbers) >= 2:
    second_largest = numbers[1]
    print("Second largest element:", second_largest)
else:
    print("The array does not have a second largest element.")
