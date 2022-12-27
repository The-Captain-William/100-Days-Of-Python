#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


class EmailReader:  # finished in 7 minutes, total 27 minutes
    def __init__(self, input_letter, input_names):
        with open(f"./input/letters/{input_letter}") as default_letter:  # open file as object
            with open(f"./input/names/{input_names}") as names:
                collection_of_names = names.read()  # read contents of names
                read_letter = default_letter.read()  # read contents of default letter
                list_of_names = collection_of_names.split()  # split contents of names into list
                print(list_of_names)  # debug
                for name in list_of_names:  # iterate over list of names
                    completed = read_letter.replace("[name]", name)  # completed text
                    with open(f"./output/readytosend/{name} Invitation letter.txt", mode="w") as compiled_letter:  # generate
                        compiled_letter.write(completed)  # write string contents into generated file


email = EmailReader("starting_letter.txt", "invited_names.txt")



# finished in 20 minutes

# with open("./input/letters/starting_letter.txt") as default_letter:  # open file as object
#     with open("./input/names/invited_names.txt") as names:
#         collection_of_names = names.read()  # read contents of names
#         read_letter = default_letter.read()  # read contents of default letter
#         list_of_names = collection_of_names.split()  # split contents of names into list
#         print(list_of_names)  # debug
#         for name in list_of_names:  # iterate over list of names
#             completed = read_letter.replace("[name]", name)  # completed text
#             with open(f"./output/readytosend/{name} Invitation letter.txt", mode="w") as compiled_letter:  # generate
#                 compiled_letter.write(completed)  # write string contents into generated file
