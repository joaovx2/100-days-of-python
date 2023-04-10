#interview question, returning a string as uppercase, lower case etc


def upper_lower(string):
    new_string = ''
    for i in range(len(string)):
        if i % 2 == 0:
            new_string += string[i].upper()
        else:
            new_string += string[i].lower()
    return new_string
user_input = input("Enter a string: ")
result = upper_lower(user_input)
print(result)