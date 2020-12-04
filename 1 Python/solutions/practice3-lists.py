


# Problem 4
# Write a function to copy all the elements of a list with value less than 10 to a new list and return it.

# def extract_less_than_ten(nums):
#     # create an empty new list
#     new_values = []
#     # copy the elements of the list nums into new_values if they're less than 10

# print(extract_less_than_ten([2, 8, 12, 18])) # [2, 8]


nums = [2, 8, 12, 18]
new_values = [] # start with an empty list
for num in nums: # iterate over each number in our list
    if num < 10: # if the number is less than 10
        new_values.append(num) # add it to our new list
print(new_values) # [2, 8]
print(nums)


# def say_hello(name):
#     print('Hello, ' + name + '!')

# name = input('what is your name? ')
# say_hello(name)

# say_hello('matthew')
