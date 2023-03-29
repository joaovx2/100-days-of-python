#printing tests
print("Day 1 - String Manipulation")
print("String Concatennation is done with the " + " Sign.")
print('e.g. Print("Hello" + "World")')
print("New Lines can be created with a backlash and a n.") 

#Printing plus getting input with variables
name = input("What is your name? ")
print("Your name is :",name)
lenght_name = len(name)
print(lenght_name)
#switching the value of variables just for fun
a = input("Digite um valor para A que sera transferido para B:")
b = input("Digite um valor para B que sera transferido para A :")
c = a
a = b
b = c
print("O valor de A trocado sera :" + a)
print("O valor de B trocado sera :" + b)


#Project test for band names
city = input("Qual e o nome da cidade em que voce nasceu?\n")
pet = input("Qual e o nome do seu animal de estimacao?\n") 
print("O nome da sua banda deve ser :\n" + city  + " " +  pet)
