##day about loops and functions
import day7_hangman_art
lives = 6
print(day7_hangman_art.logo)
choosen_word = input("Type the word that the user will be guessing : ").lower()
print(f"Choosen word is {choosen_word}")
display = []
for  _ in range(len(choosen_word)):
    display += "_"
print(display)
game_over = False
while  game_over == False: ##while NOT game_over: also works the same
    guess_letter = input("Start guessing letters from the choosen word : ").lower()#keeps asking for a new letter until game is over
    if guess_letter in display:
        print(f"The letter {guess_letter.upper()} was already guessed")
    for position in range(len(choosen_word)): #the first loop that will go through each letter  of the choosen word
        letter = choosen_word[position] 
        if letter == guess_letter: #this checks if the letter is equal to the guess
            display[position] = letter  #replaces the blanket position with the letter
    print(f"{''.join(display)}") ##displays the chosen word list with the letter replacing
    if guess_letter  not in choosen_word: ##checks if the letter is NOT in the choosen word
        lives -= 1 ##subtracts a life
        print(f"You already tried the letter {guess_letter.upper()} and it's not in the word") #tells you, you lost a life
        print(day7_hangman_art.stages[lives])#prints the asci art for the stages
        if lives == 0: #when the life is = 0 
            print("Game Over! You died.") #shows you lost the game
            game_over = True #switches the game_over to true leaving the program
    if "_" not in display: ##checks if there is empty blanekts
        game_over = True #if there no more blanket spaces
        print("You won the game! Congrats.") #show that its game over




