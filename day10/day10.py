##functions with outputs
def function_test():
    result = 10 * 10
    return result
x = 55
coisa = x * function_test()
print(coisa)
##

def format_name(f_name, s_name):
    formatted_f_name = f_name.title()
    formatted_s_name = s_name.title()
    return f"Your name should be {formatted_f_name} {formatted_s_name}"

print(format_name("Jooaofd" , "TesTe"))
#quick function to change the strings 


#function testing

def leap_year(year):
    if (year % 4 == 0):
        if (year % 100 ==0):
            if( year % 400 ==0):
                return True
            else:
                return False
        else:
            return True
    else:
        return  False
def days_in_month(year,month):
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if month not in range (1,13):
        return "Invalid Month"
    if leap_year(year) == True and month == 2:  
        return 29
    return month_days[month -1]

year = int(input("What is the year you want to check ? "))
month = int(input("Enter the month u wanna check how many days are : "))
days = days_in_month(year,month)
print(days)
##tested about returns and functions to say how many days are in a month
    