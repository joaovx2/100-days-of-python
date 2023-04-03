###scope tests####
enemies = 1

def enemy_function():
    enemies = 2
    print (f"The total of enemies inside the function : {enemies}")
    
enemy_function()
print(f"Total enemies outside the function  : {enemies}")

#this happens because ENEMIES = 2 is a local scope, and its only valid for the function, thefore if we print it outside we get 1 that was definied outside

