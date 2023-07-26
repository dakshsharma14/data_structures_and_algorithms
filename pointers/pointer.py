num1 = 11

num2 = num1

print('Before updated value is updated')
print("num1 = ", num1)
print("num2 = ", num2)

print('\nnum1 points to: ', id(num1))
print('num2 points to: ', id(num2))

num2 = 22

print('\nAfter num2 value is updated')
print("num1 = ", num1)
print("num2 = ", num2)

print('\nnum1 points to: ', id(num1))
print('num2 points to: ', id(num2))

# let's test Dictionary
# dic can't be changed as they are not immutable
dict1 = {
    'value': 11
}

dict2 = dict1

print('Before updated value is updated')
print("dict1 = ", dict1)
print("dict2 = ", dict2)

print('\nnum1 points to: ', id(dict1))
print('num2 points to: ', id(dict2))

# dict2 = {
#     'value': 22
# }
dict2['value']=22
print('After dict2 updated value is updated')
print("dict1 = ", dict1)
print("dict2 = ", dict2)

print('\ndict1 points to: ', id(dict1))
print('dict2 points to: ', id(dict2))

