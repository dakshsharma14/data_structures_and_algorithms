"""
In this program we have to calculate if the number is prime of not

what is prime? if the number has two factors 1 and itself

Steps:
First we will take the input and then initialize a variable called count which
will check if the count goes beyond 2 then not prime.

Then we will start the if statement saying that num >1 and then for loop
which says that we will go to each number from 1 to that number and check if the number
when divided gives the remainder == 0, and that particular loop we will increase the count.
And when the loop is done, it will check if the count was more than 2 then it is a prime.
"""

num = 4
count = 0

if num > 1:
    for i in range(1, num + 1):
        if (num % i) == 0:
            count = count + 1
    if count == 2:
        print("Then this number is prime")
    else:
        print("Not prime")
