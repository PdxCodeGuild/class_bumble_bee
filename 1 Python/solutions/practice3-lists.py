


import random

# Problem 1
# Write a function using random.randint to generate an random index, use that index to pick an element of a list and return it.

def random_element(a):
    i = random.randint(0, len(a)-1)
    return a[i]
#                         0         1         2
# print(random_element(['apples', 'bananas', 'pears'])) # 'apples', 'bananas' or 'pears'
# print(random_element(['apples', 'bananas', 'pears', 'cherries']))



# i = 0
# while i < 10:
#     print(i)
#     i += 1

# iterables - range, string, list, tuple, dictionary, set

# for i in range(10):
#     print(i)

# #            0          1         2
# fruits = ['apples', 'bananas', 'pears']
# for fruit in fruits:
#     fruit += '!'
#     print(fruit)
# print(fruits)

# for i in range(len(fruits)):
#     print(i, fruits[i])
#     fruits[i] += '!'
# print(fruits)

# Problem 2
# Write a function that takes a list of numbers, and returns True if there is an even number of even numbers.

def eveneven(nums):
    # step 1 - create an empty output list
    output = []
    # step 2 - iterate over input list
    for i in range(len(nums)):
        # step 3 - check if a given element from the input list is even
        if nums[i]%2 == 0:
            # step 4 - if it's even, append the element to the output list
            output.append(nums[i])
            # step 5 - if it's odd, keep it where it is
    # step 6 - if the list length % 2 gives us a remainder of 0, return true, otherwise return false
    if len(output)%2 == 0:
        return True
    return False

# def eveneven(nums):
#     output = 0
#     for num in nums:
#         if num%2 == 0:
#             output += 1
#     return output%2 == 0

# print(eveneven([5, 6, 2])) # True
# print(eveneven([5, 5, 2])) # False




# Problem 3
# Write a function that returns the reverse of a list.

# for i in range(10, 0, -1):
#     print(i)


def reverse(nums):
    
    output = nums.copy()
    output.reverse()
    return output

    # count = len(nums) - 1
    # output = []
    # while count >= 0:
    #     output.append(nums[count])
    #     count -= 1
    # return output

    # output = []
    # for i in range(len(nums)-1, -1, -1):
    #     print(i)
    #     output.append(nums[i])
    # return output

    # output = []
    # for i in range(len(nums)):
    #     # print(i, len(nums)-i-1)
    #     output.append(nums[len(nums)-i-1])
    # return output

    # output = []
    # r = list(range(len(nums)))
    # r.reverse()
    # print(r)
    # for i in r:
    #     output.append(nums[i])
    # return output

    # output = []
    # for num in nums:
    #     output.insert(0, num)
    # return output

    # output = []
    # while len(nums) > 0:
    #     output.append(nums.pop())
    # return output

# print(reverse(['a', 'b', 'c', 'd', 'e', 'f']))




# Problem 4
# Write a function to copy all the elements of a list with value less than 10 to a new list and return it.

def extract_less_than_ten(nums):
    new_values = [] # start with an empty list
    for num in nums: # iterate over each number in our list
        if num < 10: # if the number is less than 10
            new_values.append(num) # add it to our new list
    return new_values
# print(extract_less_than_ten([2, 8, 12, 18])) # [2, 8]
# print(extract_less_than_ten([5, 12, 3, 17, 9, 8, 34])) # [5, 3, 9, 8]



# Problem 5
# Write a function to find all common elements between two lists.

def common_elements(nums1, nums2):
    # step 1 - create an empty output list
    output = []
    # step 2 - iterate over the first list
    for i in range(len(nums1)):
        # step 3 - iterate over the second list
        for j in range(len(nums2)):
            # step 4 - compare values from each
            if nums1[i] == nums2[j]:
                # step 5 - if they're equal, add them to the output list
                output.append(nums2[j])
    # step 6 - return our output list
    return output

    # output = []
    # for num in nums1:
    #     if num in nums2:
    #         output.append(num)
    # return output

    # return list(set(nums1) & set(nums2))
    
# print(common_elements([1, 2, 2, 3], [2, 3, 4])) # [2, 3]


