##ceaserchiper  encrypter
import day8_imports

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def ceaser(start_text, shift_amount, direction_answer ):
    stored_text = ""
    if direction_answer == "decode":
        shift_amount *= -1
    for letters in start_text:
        position = day8_imports.alphabet.index(letters)
        new_position = position + shift_amount
        stored_text += day8_imports.alphabet[new_position]
    print(f"The {direction}d messages is the following: {stored_text}")
ceaser(start_text = text, shift_amount=shift, direction_answer=direction)