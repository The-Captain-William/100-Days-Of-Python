alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', ' ']


def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)  # find index; automatically matches like-objects
        new_position = position + shift_amount  # shift index, shift_amount is int
        if new_position > 26:
            remainder = (new_position - 27)   # 26 letters in the alphabet, or consider new_position - 25 indexes from 0 to 25; but 1 = b so 1 - 1 = 0, zeroth index.
            while remainder > 27:
                remainder -= 27
            new_position = remainder
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is: '{cipher_text}'")


def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)  # integer == alphabet index position of that same letter
        new_position = position - shift_amount  # integer == alphabet index position - shift amount
        if new_position < - 27:
            remainder = (new_position + 27)
            while remainder < -27:
                remainder += 27
            new_position = remainder
        new_letter = alphabet[new_position]  # map new letter to the alphabet list item at that new index position
        plain_text += new_letter
    print(f"The decoded text is: '{plain_text}'")


loop = True
while loop is True:
    valid = True
    direction = input("Type 'encode' to encrypt, \nType 'decode' to decrypt \n Type 'exit' to exit:\n").lower()
    if direction == "exit":
        exit()

    if direction == "encode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        encrypt(plain_text=text, shift_amount=shift)
    elif direction == "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        decrypt(cipher_text=text, shift_amount=shift)
    else:
        print("Invalid Operation")


