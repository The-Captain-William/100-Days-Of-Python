import pandas

#  TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

#  TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# import csv
nato_csv = pandas.read_csv("nato_phonetic_alphabet.csv")

# convert to dataframe
nato_dataframe = pandas.DataFrame(nato_csv)

# convert dataframe to dictionary with iloc
# iloc gives (*rows), .itterrows gives (index, row1)
nato_dict = {letter: code for (letter, code) in nato_dataframe.iloc}
print(nato_dict)  # will print dictionary to test

repeat = True

while repeat is True:
    user_words = input("Enter Word(s) here: ").upper()

    #  👀 [letter] == letter from user words, so just access key value with key
    out_put_list = [nato_dict[letter] for letter in user_words if letter in nato_dict]  # new item for item in list
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    try:
        for num in nums:
            if str(num) in user_words:
                raise ValueError("No numbers please")
    except ValueError as error:  # except = 'exception'
        print(f"{error}")  # will repeat aforementioned "no numbers" message
        repeat = True

    else:
        #  new final dictionary, using the words as a key, and the list comprehension above as a key value
        print(out_put_list)  # print output list test
        nato_transcribe = {user_words: out_put_list for words in user_words}
        print(nato_transcribe)
