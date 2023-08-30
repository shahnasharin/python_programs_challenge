#------------------------------------------- find k th largest element -------------------------------------------
numbers = [10, 5, 8, 20, 3]

k = int(input("Enter the value of k:"))


numbers.sort(reverse=True)

if 0 < k <= len(numbers):
    kth_largest = numbers[k - 1]
    print(f"{k}-th largest element:", kth_largest)
else:
    print("Invalid value of k.")
