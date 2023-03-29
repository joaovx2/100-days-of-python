#Day where im working with variables, if, else and making of multiple choice at the end
#Little program to check if the number is odd or even
number = int(input("Type the number that will be checked : "))
if number % 2 == 0:
    print(f"the {number} that you typed is even")
else:
    print(f"The {number} that you typed is odds")
    
##nested If statment for fun
name = input("What is your name ?\n")
age = int(input("What is your age ? \n"))
height = float(input("What is your Height in centimeteres ? \n"))
if height > 120:
    if age > 15:
        print(f"Your {name} are qualified")
    else:
        print(f"Due to your age being {age} you are not qualified")
else:
    print(f"Due to your height of {round(height)} centimeters you are not qualified")    
    
    
#elif stuff
height_bmi = input("Enter your Height in Meters : \n")
weight_bmi = input("Enter your Weight in KG : \n")
body_mass_bmi = round(float(weight_bmi) / float(height_bmi) ** 2)
if body_mass_bmi > 35:
    print(f"Your body mass is {body_mass_bmi} you're clinically obese.")
elif body_mass_bmi >=30:
    print(f"Your body mass is {body_mass_bmi} you're obese.")
elif body_mass_bmi >= 25:
    print(f"Your body mass is {body_mass_bmi} you're overweight.")
elif body_mass_bmi >= 18.5:
    print(f"Your body mass is {body_mass_bmi} you have normal weight.")
else:
    print(f"Your body mass is {(body_mass_bmi)} you are underweight.")
    
##checking if the year is a leap year
year = int(input("What is the year you want to check ? "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
    
##checking with IF statements for practice
year = int(input("What is the year you want to check ? "))
if (year % 4 == 0):
    if (year % 100 ==0):
        if( year % 400 ==0):
            print(f"The year {year} is a leap year")
        else:
            print(f"The year {year}, is not a leap year.")
    else:
        print(f"The year {year}, is a leap year")
else:
    print(f"The year {year}, is not a leap year.")
       
##basic logic of IF statements
#IF condition A = true
#DOES A
#IF Condition B = ALSO TRUE
#Does B
#IF Condition C = ALSO TRUE
#Do C
#For nested IF, all the conditions need to be true for the code to be executed, in this case to execute C, A and B need to be true
#
######################################
#Basic of IF but with ELIF 
#If condition A = TRUE
#DOES A
#ELIF condition B = TRUE
#DOES B, in this case, a doesnt need to be true to execute B
#ELSE
#DOES C
#in this case only one of the conditions need to be true, it will check if A is true, if its false it will go to be, if its false it will go to C Once a true statment is found
#it will skip the if block and go to the part of the code


#pizza delivery program for fun
print("Python pizza delivery program")
size = input("What size of pizza do you want, L, M or S? ?\n")
add_peperoni = input("Do you want to add peperoni ? Y or N \n")
extra_cheese = input("Do you want to add extra cheese ? Y or N \n")
total_payment = 0
if size == "L":
 total_payment+= 25
elif size == "M":
 total_payment+=20
else:
 total_payment+=15
if add_peperoni == "Y" and size == "L":
    total_payment+=3
elif add_peperoni == "Y" and size  == "M" or size == "S":
    total_payment +=2
else:
    print("No pepperoni was added")
if extra_cheese == "Y":
    print("Adding Cheese")
    total_payment +=1
    print(total_payment)
else:
    print("No cheese added")
    print(total_payment)
##


#love calculator
print("Welcome to the love calculator")
name1 = input("What is your name ?\n")
name2 = input("what is their name \n")
combinaned_name = name1 + name2
lower_name = combinaned_name.lower()
t = lower_name.count("t")
r = lower_name.count("r")
u = lower_name.count("u")
e = lower_name.count("e")
true = t + r + u + e
l = lower_name.count("l")
o = lower_name.count("o")
v = lower_name.count("v")
e = lower_name.count("e")
love = t + r + u + e
love_score = str(true)  + str(love)
love_score_int = int(love_score)
##can also be done with
# love_score = int(str(true)  + str(love))
#to wrap it around in the same line, changing the data type twice
if love_score_int < 10 or love_score_int > 90:
    print(f"your love score is {love_score}, you go together like mentos and coke")
elif love_score_int >= 40 and love_score_int <=50:
    print(f"your love score is {love_score}, you are alright together")
else:
    print(f"your love score is {love_score}, you both are dogshit together")
    
    
    








    
