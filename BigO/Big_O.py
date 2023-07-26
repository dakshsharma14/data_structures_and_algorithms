# if we talk about the Big O

# O(n) number of operation
def print_items(n):
    for i in range(n):
        print(i)


print_items(2)


# # Drop the constants O(2n) => O(n)
def print_items(n):
    for i in range(n):
        print(i)

    for j in range(n):
        print(j)


print_items(2)


# O(n^2)
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)


print_items(2)


# Drop Non Dominants
# O(n^2 + n) => O(n^2) ; n^2 >>>>> n
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

    for k in range(n):
        print(k)


print_items(2)


# O(1)
def add_items(n):
    return n + n

