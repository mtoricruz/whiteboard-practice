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
# Single dictionary with 4 k/v pairs
# 4 strings / 4 integers
# return sum of integers
# if i want an algo to return sum integers, create an empty list to store those numeric values
# if type(x) checks if it's int/str/etc.

# P
numbers = []
for k, v in d.items():
    if type(v) is int:
        numbers.append(v)
total = sum(numbers)
print(total)


        