
# def my_function():
#    for i in range(1, 20):
#      if i == 20:
#         print("You got it")
# my_function()
# first bug is related to the RANGE function, its only going to the number 19, due to how the function works, you need to specify 21 for the number 20 to be included
#solution is range(1,21)


# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])
#In this case, the problem is the radint, its going to the value 6, when the list starts from 0 so the maximum value is 5
#solution is radint(0,5)





# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")
#solution is a >= so when u type 1994 ONE of the IF statements can be triggered




# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")
#identation error, print should be indented in the IF statement


# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)
#there is a double = sig checking for equality, resulting in the variable words_per_page keeping the 0 value and not changing
#solution is replace the double = with just an = 


# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)
# mutate([1,2,3,5,8,13])
#simple problem, the b_list.append is not indented correcntly, so only the LAST value of the a_list is being multiplied
# #solution is indenting the b_list to the for loop
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)
