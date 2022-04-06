# You are given a two-digit integer n. Return the sum of its digits.

# Example

# For n = 29, the output should be
# solution(n) = 11.

# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] integer n

# A positive two-digit integer.

# Guaranteed constraints:
# 10 ≤ n ≤ 99.

# [output] integer

# The sum of the first and second digits of the input number.

# [Python 3] Syntax Tips

# # Prints help message to the console
# # Returns a string
# def helloWorld(name):
#     print("This prints to the console when you Run Tests")
#     return "Hello, " + name




# solution:
def solution(n):
    d1 = n%10
    d2 = (n-d1)/10
    return d1+d2