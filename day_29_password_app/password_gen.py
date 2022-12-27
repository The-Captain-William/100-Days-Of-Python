import random


def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    collection = [(random.choices(letters, k=8), random.choices(numbers, k=6), random.choices(symbols, k=6))]
    # generates list tuple lists
    password_list = []

    for the_tuple in collection:  # for the tuple in the list
        for lists in the_tuple:  # for the lists in the tuple
            for item in lists:  # for all the items in each of the lists
                password_list.append(item)  # append every item to the pw_list

    random.shuffle(password_list)
    password = ''.join(password_list)  # empty + char for every char in pw_list
    return password
