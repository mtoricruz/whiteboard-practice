# Print out all of the numbers in the following array that are divisible by 3:

numbers = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]

# The expected output for the above input is:
# 27
# 81
# 9
# 27
# 99
# 63
# 42

# You may use whatever programming language you wish.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.

# U - Print out all numbers in given array that are divisble 3
# each number has to be printed on their own line
# Looping through array to check if number is divisble 3 and then print
# if not divisble 3, continue looping through list

# P - 
# Loop numbers
# for each number in numbers_array:
    # check if number is divisible 3:
        # print(number)

# E -

for num in numbers:
    if num % 3 == 0:
        print(num)

