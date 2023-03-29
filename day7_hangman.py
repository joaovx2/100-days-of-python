##day about loops and functions
choosen_word = input("Type the word that the user will be guessing : ").lower()
print(f"Choosen word is {choosen_word}")
display = []
for  _ in range(len(choosen_word)):
    display += "_"
print(display)
game_over = False
while  game_over == False: ##while NOT game_over: also works the same
    guess_letter = input("Start guessing letters from the choosen word : ").lower()#keeps asking for a new letter until game is over
    for position in range(len(choosen_word)): #gets the positions in the range of the choosen word
        letter = choosen_word[position] 
        if letter == guess_letter: #this replaces the display of the choosen word with the right letter if it the case
            display[position] = letter 
    print(display) ##displays the chosen word list with the letter replacing
    if "_" not in display: ##checks if there is empty blanekts
        game_over = True #if there no more blanket spaces
        print("Game Over.") #show that its game over


