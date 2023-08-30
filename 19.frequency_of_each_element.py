# ---------------------------------frequency  of each elements---------------------------------------------


elements = [1, 2, 2, 3, 1, 4, 5, 3, 2, 4, 4]

# Initialize an empty dictionary to store the counts
element_counts = {}

# Iterate through the list and count the frequency of each element
for element in elements:
    if element in element_counts:
        element_counts[element] += 1
    else:
        element_counts[element] = 1

# Print the frequency of each element
for element, count in element_counts.items():
    print(f"Element {element} appears {count} times")

#------------------------------------------------------------------------------------------------------------
# output:
# Element 1 appears 2 times
# Element 2 appears 3 times
# Element 3 appears 2 times
# Element 4 appears 3 times
# Element 5 appears 1 times
