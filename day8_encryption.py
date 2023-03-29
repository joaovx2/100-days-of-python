##ceaserchiper  encrypter
import day8_imports
def encrypt(text_encrypt,shift_encrypt):
    encrypted_text = ""
    for letters in text_encrypt:
       position = day8_imports.alphabet.index(letters)
       new_position = position + shift_encrypt
       new_letter = day8_imports.alphabet[new_position]
       encrypted_text +=  new_letter
    print(encrypted_text)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
encrypt(text_encrypt = text, shift_encrypt = shift)
