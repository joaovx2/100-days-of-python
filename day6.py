##loops and shit like that
weapons = ["Scythe", "Sword", "Katana", "Bow and Arrow", "Crossbow"]
for weapon in weapons: ##assigns the variable WEAPON for the list WEAPONS
    print(weapon)


###average height of many students
students_heights = [183, 192, 175 ,177 ,176 ,155 ,154 ,161 ,164 ,168]
extra_student = int(input("Add the extra student height in centimeters.\n"))
students_heights.append(extra_student)
total = 0 
i = 0
amount = 0
print(students_heights)
for i in  students_heights:
    total += i  ##this adds the numbers from the list together, 183+192+175+... all the way until the last one
for n in students_heights:
    amount += 1
average = total / amount
print(f"The average Height in the class of {amount} students is {round(average,2)}.")
#this is done without using the len function to get the number of elements in the list, or the sum function to get the total
#just to memorize for loops and how they can be used


   