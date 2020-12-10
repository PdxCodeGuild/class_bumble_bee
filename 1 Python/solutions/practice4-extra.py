


# Problem 1: Pretty Numbers
# Convert an integer into a pretty string with commas 12345678 to 12,345,678


# indices: 0123456789
# number:  1653872151

#         0 123 456 789
# output: 1,653,872,151



def pretty_number(num):
    num = str(num)
    num = list(num)
    num.reverse()
    output = []
    for i in range(len(num)):
        output.append(num[i])
        # if you're at an increment of 3
        # and NOT on the last iteration
        # add a comma
        if (i+1)%3 == 0 and i+1 < len(num):
            output.append(',')
    output.reverse()
    output = ''.join(output)
    return output

    # num = str(num)
    # output = ''
    # for i in range(len(num)-1, -1, -1):
    #     output = num[i] + output
    #     if (len(num)-i)%3 == 0 and i != 0:
    #         output = ',' + output
    # return output

    # num = str(num)
    # output = ''
    # for i in range(len(num)//3, -1, -1):
    #     output = ',' + num[i*3: i*3+3] + output
    # return output
    


#                    indices       9 876 543 210
# print(pretty_number(1653872151)) # 1,653,872,151
# print(pretty_number(2358109322348520)) # 2,358,109,322,348,520
# print(pretty_number(999999)) # 999,999
# print(pretty_number(0)) # 0
# print(pretty_number(999)) # 999
# print(pretty_number(10000)) # 10,000



# Problem 12
# Write a function that takes n as a parameter, and returns a list containing the first n Fibonacci Numbers.
# 

def fibonacci(n):
    output = []
    for i in range(n):
        if i == 0 or i == 1:
            output.append(1)
        else:
            output.append(output[i-1] + output[i-2])
            # output.append(output[-1] + output[-2])
    
    # if n == 1:
    #     return [1]
    # output = [1, 1]
    # for i in range(n-2):
    #     output.append(output[-1] + output[-2])


    return output


print(fibonacci(1)) # [1]
print(fibonacci(2)) # [1, 1]

print(fibonacci(8))  # [1, 1, 2, 3, 5, 8, 13, 21]
print(fibonacci(10)) # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]