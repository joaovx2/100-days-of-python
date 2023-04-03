import day11_art
import random
import os

def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score): 
  """Compare the user and the computer score situations"""
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"
  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def play_game(): ##definies the function play game, that will keep playing the game until the user says 'n'

  print(day11_art.logo) #prints the logo

  user_cards = [] #gives the user a list of empty cards
  computer_cards = [] #gives the computer a empty list of card
  is_game_over = False #definies the boolean for the game situation

  for _ in range(2): #a loop to deal 2 cards for each player
    user_cards.append(deal_card())
    computer_cards.append(deal_card())


  while not is_game_over: #WHILE the boolean is false, the loop continues
    user_score = calculate_score(user_cards) #calculates the score of the list of cards for the players
    computer_score = calculate_score(computer_cards) #same fo rhte computer
    print(f"   Your cards: {user_cards}, current score: {user_score}") #prints out the values
    print(f"   Computer's first card: {computer_cards[0]}") #prints the computer values
 
    if user_score == 0 or computer_score == 0 or user_score > 21: #checks the situation, if you get a black jack or computer gets a black jack its game over
      is_game_over = True #if this is true, jumps out of the while loop
    else:
      user_should_deal = input("Type 'y' to get another card, type 'n'  to pass: ") #checks if the user wants another card or not
      if user_should_deal == "y":
        user_cards.append(deal_card()) #adds a card to the user list
      else:
        is_game_over = True

  while computer_score != 0 and computer_score < 17: #while the computer is less than 17 it will keep asking for more cards
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  os.system("cls")
  play_game()
