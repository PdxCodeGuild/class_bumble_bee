

def get_integer(text):
    while True:
        value = input(text)
        if value.isdigit():
            return int(value)
        print('please enter an integer')

