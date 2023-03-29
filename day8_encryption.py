##ceaserchiper  encrypter
import day8_imports
print(day8_imports.logo)
running = True
while running == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26 ##this is to make sure the shift will always be inboud of the list for example, if its shift 45, 45 % 26 is 19, so position 19 will be used exmaple 26+19 = 45
    def ceaser(start_text, shift_amount, direction_answer ): ##definies ceaser function for encryption
        stored_text = "" #will create a variable to hold the string result
        if direction_answer == "decode": #checks if it was written decode or encode 
            shift_amount *= -1 #if it was decode, it will flip the switch amount to a negative number, lets say it was written shift by 2 this would make -2
        for letters in start_text: #goes through each letter in the user input for the messsage
            if letters in day8_imports.alphabet: #checks if the letter/typed character IS really IN THE ALPHABET
                position = day8_imports.alphabet.index(letters) #gets the position of each letter in the message in  a  loop, 
                new_position = position + shift_amount #gets the new position based on alphabeter position + shift amount, EX shift = 2, Word Amor, A position 0 would be C after a +2 shift
                stored_text += day8_imports.alphabet[new_position] #stores letters into a string that will be printed
            else: #if its NOT in the alphabet will be ignored, so spaces, symbols and numbers can go through
                stored_text += letters
        print(f"The {direction}d messages is the following: {stored_text}") #printes the stored variable
    ceaser(start_text = text, shift_amount=shift, direction_answer=direction)
    answer = input("Do you wanna continue Yes or No ? ").lower()
    if answer == "no":
        running = False
        print("Adios")