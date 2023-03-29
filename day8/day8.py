##start of day 8
import math
def name_location(name, location):
    print(f"Hello, {name}")
    print(f"How is it to live at,{location}")
teste = input("What is your name ?\n")
teste2 = input("Where do you live ?\n")
name_location(teste, teste2)
###function to calculate how many cans to paint a wall
teste_h = int(input("What is the height of the wall ? \n"))
teste_w = int(input("What is the width of the wall ? \n"))
coverage = 5 ##square meters per can of paint
def calculator_can(height = teste_h, width = teste_w, cover = coverage):
    area = (height * width)
    final = area / coverage
    final_value = math.ceil(final)
    print(f"The number of cans that you need to buy are : {final_value}")
calculator_can()
#function to calculate if a number is a prime number or no
def prime_checker(number):
    prime = True
    for i in range(2, number):
        if number % i == 0:
            prime = False
    if prime:   
        print(f"The number {number} is a prime number")            
    else:
        print(f"{number} is not a prime number")
n = int(input("Tell me what number you wanna check : "))
prime_checker(number = n)

