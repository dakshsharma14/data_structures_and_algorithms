"""
How to find the factorials of this number

Here we will find the factorial by multiplying each number before the given number and itself
"""

factorial = 1
num = 5

if num < 0:
    print("factorial does not exists")
elif num == 0:
    print("The factorial is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("The factorial is", factorial)


####################################################
# another way recursion
# 5 * (5-1) * (4-1) * (3-1).... call the same method again and again


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))
