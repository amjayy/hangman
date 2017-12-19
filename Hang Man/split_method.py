words= 'cat', 'dog', 'hamster', 'chicken'.split()
# takes a string in python and converts it to a list variable. each space creates a new element list

def get_name():
    #Ask user their name and return name.
    name = input("What is your name?").capitalize()
    return name

def long_name():
    # Ask user name and then capitialize.
    name = input (' What is your name?')
    new_name = name.split()

    final_name = ' '

    for i in new_name:
        final_name += i.capitalize()
        final_name += ' '

    return final_name.strip()
