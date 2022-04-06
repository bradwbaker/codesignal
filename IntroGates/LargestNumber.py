# Given an integer n, return the largest number that contains exactly n digits.

# Example

# For n = 2, the output should be
# solution(n) = 99.

# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] integer n

# Guaranteed constraints:
# 1 ≤ n ≤ 9.

# [output] integer

# The largest integer of length n.

# [Python 3] Syntax Tips

# # Prints help message to the console
# # Returns a string
# def helloWorld(name):
#     print("This prints to the console when you Run Tests")
#     return "Hello, " + name



# solution:
def solution(n):
    temp = 0
    for x in range(0,n):
        temp += 9*pow(10,x)
    return temp