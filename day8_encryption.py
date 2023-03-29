##ceaserchiper  encrypter
import day8_imports

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount): ##pass in the arguments
  cipher_text = "" #the string that will store the final value of the encrypted message
  for letter in plain_text: #for every letter in the plain_text, which is the user response
    position = day8_imports.alphabet.index(letter) #the position will be the index of the alphabet, so position 0 is A
    new_position = position + shift_amount #new position is position + shift amount
    cipher_text += day8_imports.alphabet[new_position] #the string will will recieve the value, ends the loop
  print(f"The encoded text is {cipher_text}") #after the loop ends it prints the value
     
def decrypt(cipher_text, shift_amount): #arguments to decrypt
  plain_text = "" #string taht will store the value fo the decrypted message
  for letter in cipher_text: #for every letter in the cipher_text = user input
    position = day8_imports.alphabet.index(letter) #the position will be storing the index value of the user input, so if the user says A will be 0 again
    new_position = position - shift_amount #the position will be the current position - 5
    plain_text += day8_imports.alphabet[new_position] #the string will be recieving letter by letter until ends the loop
  print(f"The decoded text is {plain_text}") #prints the decode message

if direction == "encode": #if the direction (user input is encode) calls out the function to encrypt
  encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode": #if the direction( user input is decode) calls out the function to decode
  decrypt(cipher_text=text, shift_amount=shift)
