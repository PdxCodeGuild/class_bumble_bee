

import string


# Problem 1
# Get a string from the user, print out another string, doubling every letter.

def multiply_letters(word, n):
    # accumulator pattern
    output = ''
    for char in word:
        # output += char + char
        output += char * n
    return output

    # return ''.join([char*2 for char in word])

# print(multiply_letters('hello', 40)) # hheelllloo


# Problem 2 ========================================
# Return the number of letter occurances in a string.

def count_letter(letter, word):

    total = 0
    for char in word:
        if char == letter:
            total += 1
    return total


    # return word.count(letter)

    # initial_length = len(word)
    # word = word.replace(letter, '')
    # final_length = len(word)
    # return initial_length - final_length

# print(count_letter('i', 'antidisestablishmentterianism')) # 5
# print(count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis')) # 2


# Problem 3
# Return the letter that appears the latest in the english alphabet.

def latest_letter(word):

    # option 1 - sort and take the latest letter

    word_list = list(word)
    word_list.sort()
    return word_list[-1]

    # option 2 - convert to ascii code, find the largest ascii value
    # convert to lower case first

    # word = word.lower()
    # highest = 0
    # for char in word:
    #     if ord(char) > highest:
    #         highest = ord(char)
    # return chr(highest)

    # option 3 - combine options 1 and 2
    # codes = []
    # for char in word:
    #     codes.append(ord(char))
    # codes.sort()
    # return chr(codes[-1])

    # option 4 - use the alphabet and .find
    # alphabet = string.ascii_lowercase
    # highest = 'a'
    # for char in word:
    #     if alphabet.find(char) > alphabet.find(highest):
    #         highest = char
    # return highest
    




print(latest_letter('Pneumonoultramicroscopicsilicovolcanoconiosis')) # v

# print(latest_letter('aZ')) # a

