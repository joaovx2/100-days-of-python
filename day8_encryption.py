##ceaserchiper  encrypter
import day8_imports

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def ceaser(start_text, shift_amount, direction_answer ): ##definies ceaser function for encryption
    stored_text = "" #will create a variable to hold the string result
    if direction_answer == "decode": #checks if it was written decode or encode 
        shift_amount *= -1 #if it was decode, it will flip the switch amount to a negative number, lets say it was written shift by 2 this would make -2
    for letters in start_text: #goes through each letter in the user input for the messsage
        position = day8_imports.alphabet.index(letters) #gets the position of each letter in the message in  a  loop, 
        new_position = position + shift_amount #gets the new position based on alphabeter position + shift amount, EX shift = 2, Word Amor, A position 0 would be C after a +2 shift
        stored_text += day8_imports.alphabet[new_position] #stores letter by letter in the string we created
    print(f"The {direction}d messages is the following: {stored_text}") #after the loops ends prints out the message coded or decode
ceaser(start_text = text, shift_amount=shift, direction_answer=direction) #calls out the function