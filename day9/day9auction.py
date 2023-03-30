import time
import day9_arts
import os


print(day9_arts.logo)

bids = {} ##definies the bid dictionary
bidding_finished = False #definies that while bidding finish is false theg ame wil continue asking for more people

def find_highest_bidder(bidding_record): ##definies a function, that will find the highest bid amount and name
  highest_bid = 0 #declares the highest bid starting from 0
  winner = "" #declares winner is a string
  for bidder in bidding_record: #for every bidder in the bidding_record dictionary
    bid_amount = bidding_record[bidder] #bid amount is equal to the VALUE of the bid that the BIDDER did, for example Joao : 20, highest bid will be 20
    if bid_amount > highest_bid:  #tests if the bid amount is higher than the highest_bid, that will start with 0
      highest_bid = bid_amount #if it is, the highest bid will be the bid amount, the VALUE of the KEY fo the dictionary
      winner = bidder #the name will be the key of, so in thsi case the key would be joao, since the dictionary is structered as a Key:Value
  print(f"The winner is {winner} with a bid of ${highest_bid}")#prints out
  
while not bidding_finished:  #checks iof the bidding is finished or not, while this is false it will keep looping
  name = input("What is your name?: ") 
  price = int(input("What is your bid?: $"))
  bids[name] = price #this will get the user input for the dictionarry, so name will be the key, price the value of the BIDS dictionary
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n") #user input if it should end the game or not
  if should_continue == "no": #if its time to finished, the biddinf_finished variable will be true, will call out the function to find the highest bidder and end
    bidding_finished = True ##changes variable to true jumpin out of the while loop
    find_highest_bidder(bids)
    time.sleep(2)
  elif should_continue == "yes": #if its yes, will ask for name and price again
    os.system("cls") #clears the screen to ask for another input
  
