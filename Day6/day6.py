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
for i in  students_heights:
    total += i  ##this adds the numbers from the list together, 183+192+175+... all the way until the last one
for n in students_heights:
    amount += 1
average = total / amount
print(f"The average Height in the class of {amount} students is {round(average,2)}.")
#this is done without using the len function to get the number of elements in the list, or the sum function to get the total
#just to memorize for loops and how they can be used


students_score = [66, 91, 90 ,77 ,76 ,55 ,54 ,61 ,64 ,68,92]
Added_score = int(input("Add the extra score.\n"))
students_score.append(Added_score)
highest_score = 0
for score in students_score: ##SCORE IS THE ELEMENT, STUDENTS_SCORE IS THE LIST
    if score > highest_score:
         highest_score = score ##this for example needs to be referred by score, the INT ELEMENT, inside the list
print(highest_score)
#this can be done with the max function, but for testing purpouses we are using the for loops

##range function
#sum of every number from 1 to 100
total_sum = 0
for number in range(1, 101):
    total_sum += number
print(total_sum)
##every even number from 1 to 100 using range function 
even = 0
for number in range(2 ,101, 2):
    even += number
print(even)
##




   