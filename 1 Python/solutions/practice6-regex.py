

import re
import requests

# regex = r'\(?\d{3}[- )\.]*\d{3}-?\d{4}'

# phone_numbers = [
#     '555-555-5555',
#     '123-456-7',
#     '123',
#     'abc-def-ghij',
#     '123-456-7890',
#     '(123) 456-7890',
#     '1234567890',
#     '123) . 4567890'
# ]
# for phone_number in phone_numbers:
#     print(phone_number, re.match(regex, phone_number))
    


# phone_numbers = '''555-555-5555
# 123-456-7
# 123
# abc-def-ghij
# 123-456-7890
# (123) 456-7890
# 1234567890
# 123) . 4567890'''
# print(re.findall(regex, phone_numbers))





# response = requests.get('https://www.google.com')
# print(re.findall(r'#[a-fA-F0-9]{3,6}', response.text))



# Problem 1: Validate an Email Address
# Write a function validate_email_address which returns True if the given string is an email address, False is it isn't.

def validate_email_address(email):
    email_regex = r'^\w+@\w+(\.\w+)+'
    match = re.match(email_regex, email)
    if match is None:
        return False
    else:
        return True

# test_values = [
#     ('test@gmail.com', True),
#     ('abc123@hotmail.co.uk', True),
#     ('test@gmail___', False),
#     ('test@gmail___', False),
#     ('test@gmail', False),
#     ('test@gmail@com', False)
# ]
# for test_value in test_values:
#     if validate_email_address(test_value[0]) == test_value[1]:
#         print(test_value[0], 'pass', sep='\t\t')
#     else:
#         print(test_value[0], 'fail', sep='\t\t')




# Problem 2: Validate a Phone Number
# write a function to clean up a phone number

def validate_phone_number(phone_number):
    phone_number_regex = r'^\(?(\d{3})[\)\- \.]*(\d{3})[\- \.]*(\d{4})$'
    match = re.match(phone_number_regex, phone_number)
    if match is None:
        return None
    groups = match.group(1,2,3)
    output = groups[0] + '-' + groups[1] + '-' + groups[2]
    return output


print(validate_phone_number('0123456789')) # 0123456789
print(validate_phone_number('012-345-6789')) # 0123456789
print(validate_phone_number('(012) 345-6789')) # 0123456789
print(validate_phone_number('012-3A5-6789')) # None
print(validate_phone_number('1-1-1')) # None