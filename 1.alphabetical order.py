# Qn:Write aprogram that takes a user's name as input
# and then sorts the characters in the name in alphabetical order..?

# input:james
# output:aejms

#--------------------------------------------------------------------------------------------------------------------

name = input("Enter your Name: ")

sorted_name = ''.join(sorted(name))

print(f'Your Sorted Name Is: {sorted_name}')



