#---------------------------- merge two unsorted array in to sorted array------------------------------

array1 = [5, 1, 3, 7]
array2 = [9, 2, 6, 4]

combined_list = array1 + array2

merged_sorted_array = sorted(combined_list)

print("Merged and Sorted Array:", merged_sorted_array)

#------------------------------------------PROBLEM -2- -----------------------------------------

input_first_array=input('enter first array:')
input_second_array=input('enter second array:')

a =[int(num) for num in input_first_array.split()]
b =[int(num) for num in input_second_array.split()]

compined_array =a+b

sorted_array = sorted(compined_array)

print(sorted_array)