##password generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password = ""
random_pass_letters = random.choices(letters, k=nr_letters) ##choices will get a random value from the LIST, K=NUMBER OF ELEMENTS, IN THIS CASE ELEMENTS ARE INPUT USER
random_pass_symbols = random.choices(symbols, k=nr_symbols)
random_pass_numbers = random.choices(numbers, k=nr_numbers)
password_list = [y for x in [random_pass_letters, random_pass_numbers, random_pass_symbols] for y in x]
random.shuffle(password_list)
print ("".join(password_list))
## one way to do it using random.choices functions, and shuffle function
#################################################################################################################################################################################################################
#second way to do it
print("Second way to do it, code test!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password_testes = []
for char in range (1, nr_letters +1):
    password_testes.append(random.choice(letters))
for char in range (1, nr_numbers +1):
    password_testes.append(random.choice(numbers))
for char in range (1, nr_symbols +1):
    password_testes.append(random.choice(symbols))
random.shuffle(password_testes)
password_final = ""
for char in password_testes:
    password_final += char
print(f"Final password second way, {password_final}")