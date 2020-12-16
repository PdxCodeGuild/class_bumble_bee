





import random

def random_list(n):
    '''Generates a list of random numbers'''
    random_list = []
    for _ in range(n):
        random_list.append(random.randint(0,99))
    return random_list




# Fisher-Yates Shuffle

# iterate through the indices of the list
# for each iteration, generate a random index
# swap the elements at the two indices

# for i from 0 to n−1 do
#      j ← random integer such that i ≤ j < n
#      exchange a[i] and a[j]

#  i        j
# [1, 2, 3, 4, 5, 6]
# [4, 2, 3, 1, 5, 6]

#  j  i
# [4, 2, 3, 1, 5, 6]
# [2, 4, 3, 1, 5, 6]

#        i        j
# [2, 4, 3, 1, 5, 6]
# [2, 4, 6, 1, 5, 3]

def shuffle(nums):
    '''Randomly re-arranges a list'''
    for i in range(0,len(nums)):
        j = random.randint(i,len(nums)-1)
        # print(f"i:{i} j:{j}")  
        t_num = nums[i] 
        nums[i] = nums[j]
        nums[j] = t_num

        # nums[i], nums[j] = nums[j], nums[i]
    



def is_sorted(nums):
    '''Checks if a list is sorted'''
    for i in range(len(nums)):
        if i + 1 < len(nums) and nums[i] > nums[i + 1]:
            return False
    return True


def bogosort(nums):   
    '''bogosort(nums) continues to generate random arrangements until the list is sorted'''
    shuffle(nums)
    return is_sorted(nums)


nums = random_list(10)
# nums.sort()
print(nums)
# shuffle(nums)
# print(is_sorted(nums))

count = 0
while True:
    if bogosort(nums):
        print(nums)
        print(f"success {count}")
        break
    count += 1

