#day2 pretty much but more random easier things for fun
#Data type playing around
print("Hello"[4])

#printing integer
print(25+50)

#floats
print(3.1415)

#booleans to test if situations are true or false


#basic conversions
#len will get an INT value, to CONCATENATE with STR we convert it STR using the str function for the variable that recieves the result of the input of the user
character_name = len(input("What is your name?\n"))
str_character_name = str(character_name)
print("Your name has " + str_character_name  + " amount of characters.")

#basic integer stuff
first_number = input("Digite o primeiro numero : ")
second_number = input("Digite o Segundo numero : ")
addition = int(first_number) + int(second_number)
print(type(addition))
str_addition = str(addition)
print("O resultado seria " + str_addition + " penes" )

#Caso seja feito uma soma dos DIGITOS de um numero
number = input("Digite um numero de dois digitos : \n")
first_digit = number[0]
second_digit = number[1]
result = int(first_digit) + int(second_digit)
print("O resultado da soma dos 2 digitos seria : ", result)

#bmi calculator
height = input("Enter your Height in M : \n")
weight = input("Enter your Weight in KG : \n")
body_mass = float(weight) / float(height) ** 2
print(body_mass)

#calculating how many weeks are left until someone is 90 years old
age = input("What is your current age ? \n")
#converting the age to int, due to the INPUT function always getting a string
age_int = int(age)
years_remaining = 90 - age_int
days_remaining = years_remaining * 365 
months_remaining = years_remaining * 12
weeks_remaining = years_remaining * 52
final_message = f"You have {years_remaining} Years remaining,{months_remaining} Months remaining, {weeks_remaining} weeks remaining"
print(final_message)


#tip calculator to test the basic logics of operations and programming
print("Time to calculate something for fun\n")
bill_value = input("What was the total bill ? \n")
tip_value = input("How much percentage do you want to give it as a tip ? \n")
people_value = input("How many people are splitting the bill? \n" )
tip_percentage =  float(tip_value)  / 100
tip_total = tip_percentage + 1
bill_value_final =  float(bill_value) * float(tip_total)
final_result = float(bill_value_final) / int(people_value)
rounded_result = round(final_result, 2)
if rounded_result > 20:
    print("The total amount that should be payed per person is " + str(rounded_result) + " You just became completely broke")
else:
    print("The total amount that sohuld be payed per person is " + str(rounded_result) + " Its a fine amount to pay ")




