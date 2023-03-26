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