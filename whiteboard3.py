# Add up and print the sum of the all of the minimum elements of each inner array:
array = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
# The expected output is given by:
# 4 + -1 + 9 + -56 + 201 + 18 = 175
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.

# U
# I need to access each inner array inside the outer array. 
# The inner arrays only go 1 level deep
# Each item in the arrays are integers
# When I access the inner array, I need to loop through the values
# and determine the lowest interger
# After I determine smallest number in each inner array
# i need to add them up and print the sum of all of the smallest integers
# create an empty list to store smallest values
# then add up total of the values in that list

# P

# sum_of_values = []

# for i in array:
#   sort inner lists
#   append value of 0 index to sum_of_values list
# store total in a variable with sum(method)
# total = sum(sum_of_values)
# print(total)

sum_of_values = []

for i in array:
    i.sort()
    sum_of_values.append(i[0])

total = sum(sum_of_values)

print(total)
        



