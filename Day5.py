#day about lists, randomization and etc
import random
random_float = random.uniform(0,5)
#random.uniform() returns for a range specified includes specified values
#random.random() range of 0 to 1 doenst include 0 and 1
#random.radint() returns value of a int and can be specified, includes the specified value
print(random_float)

##tail or heads random
result = random.randint(0,1)
if result == 0:
    print("Heads")
else:
    print("tails")
    
list = ["casa","sexo","penis","teste","pinto","cu","bosta","mijo"]
list.append("test")
#append function adds an item to the end of the list
list.extend(["test2","test3"])
#extended, adds a bunch of itens to the end of the list
#can also substitute a value by using
list[3] = "test subs"
print(list[3])
print(list[-1])
#len prints lenght of the list
print(len(list))

##banker roullete test
names_string = input("Give me everyone's names separated by a comma and a space.")
names_list = names_string.split(", ")
#split function splits a string using a divider, in this case a ", ", turning the names_list variable into a list type variable
random_index = random.randrange(len(names_list))
##after i get the list, random_index variable will recieve a random number for the position that will be selected into the list, so using the random.ranrange, we get the 
#LENGHT OF THE LIST
random_selected = names_list[random_index]
#after getting the random number, we will atribuite a variable, Random_selected, that is the POSITION in the LIST that will be prited
print(f"Today {random_selected}, will be paying the bill")
##test of using random function to print out someone from a list










