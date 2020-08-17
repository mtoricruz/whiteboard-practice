# Given an object/dictionary with keys and values that consist of both strings and integers, design an algorithm to calculate and return the sum of all of the numeric values.
# For example, given the following object/dictionary as input:
d = {
  "cat": "bob",
  "dog": 23,
  19: 18,
  90: "fish"
}
# Your algorithm should return 41, the sum of the values 23 and 18.
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.
# U
# I'm given an object, that must RETURN an integer of 41.
# The values of 23 & 18 which are the keys 
# Create a def function to be able to return the sum - optional
# loop through items in dictionary
# if i only need to integers, i need logic to separate string from integers.
# get total of integers and either return or print sum

# P
# Loop through dictionary
    # check if value is integer
    # if integer
# total = []
# E
# for i in d:
#     if type(d[i]) == int:
#         total.append(d[i])

# total_sum = sum(total)
# print(total_sum)

total = 0
for i in d:
    if type(d[i]) == int:
        total += d[i]
print(total)