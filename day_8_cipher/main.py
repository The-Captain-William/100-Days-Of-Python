# project cesar

def cesar(text, shift_amount, coding):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z', ' ']

    if coding == "encode":
        cipher_text = ""
        for letter in text:
            if letter in alphabet:
                position = alphabet.index(letter)  # find index; automatically matches like-objects
                new_position = position + shift_amount  # shift index, shift_amount is int
                if new_position > 26:
                    remainder = (
                            new_position - 27)  # 26 letters in the alphabet + space, or consider new_position - 27 indexes from 0 to 27; but 1 = b so 1 - 1 = 0, zeroth index.
                    while remainder > 27:  # 27 is the index range limit
                        remainder -= 27
                    new_position = remainder
                new_letter = alphabet[new_position]
                cipher_text += new_letter
            else:
                cipher_text += letter
        print(f"The encoded text is: '{cipher_text}'")

    if coding == "decode":
        plain_text = ""
        for letter in text:
            if letter in alphabet:
                position = alphabet.index(letter)  # integer == alphabet index position of that same letter
                new_position = position - shift_amount  # integer == alphabet index position - shift amount
                if new_position < - 27:
                    remainder = (new_position + 27)
                    while remainder < -27:  # -27 is the range limit (-27 == a)
                        remainder += 27
                    new_position = remainder
                    new_letter = alphabet[new_position]  # map new letter to the alphabet list item at that new index position
                    plain_text += new_letter
            else:
                plain_text += letter
        print(f"The decoded text is: '{plain_text}'")



def cipher_greet():
    valid = True
    while valid is True:
        direction = input("Type 'encode' to encrypt, \nType 'decode' to decrypt, \nType 'exit' to exit:\n").lower()
        if direction == "exit":
            exit()

        if direction == "encode":
            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))
            cesar(text=text, shift_amount=shift, coding='encode')
        elif direction == "decode":
            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))
            cesar(text=text, shift_amount=shift, coding='decode')
        else:
            print("Invalid Operation")

cipher_greet()