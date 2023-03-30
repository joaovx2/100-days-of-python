##day9
students_score = {
    "Harry" : 81,
    "John" : 99,
    "Alice" : 88,
    "Rukia" : 67
}
students_grade = {}
for student in students_score: #this is for the KEY only, will loop through the students
    score = students_score[student] #this will be to  give the score variable the VALUE of the dictionary, in this case 81, 99, 88
    if score > 90:  #tests if the value(score) 
        students_grade[student] = "Incredible" #if it is higher than 90, will give the STUDENT and the value INCREDIBLE to the empty dictionary students_grade
    elif score > 80 and score < 90:
        students_grade[student] = "Very good"
    else:
        students_grade[student] = "Failed "
print(students_grade)
#############################################
###nesting 
weapons = {
    "Scythe" : {"Description " : "The best weapon ever"  , "Attack_Power" : 99, "Magic_Power" : 90},
    "Sword" : {"Description" : "The sword was used by the ancients", "Attack_Power" : 95, "Magic_Power": 92},
    "Staff" : {"Description" : "The staff was used my Merlin", "Attack_power" : 70, "Magic_Power" : 99}
}
print(weapons["Scythe"])

#nesting dictionary
#adding new input to the travel_log dictionary

travel_log = [
{
  "country": "France", 
  "cities_visited": ["Paris", "Lille", "Dijon"], 
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},
]

##function to add a new item o the dictioanry
def add_new_country(country_visited, times_visited, cities_visited): ##definies a function to add the country and its keys and values
    new_country = {} ##defining a empty dictionary to recieve the values
    new_country["Country"] = country_visited # in the empty dictionary, adds to the country list
    new_country["Total_Visits"] = times_visited #in the empty dictionary, adds to the total visits
    new_country["Cities_Visited"] = cities_visited #in the emppty dictionary, adds to the cities visited
    travel_log.append(new_country) #appends the dictionary related to the country, cities, and total visits to the list of dictioanry
add_new_country("Russia",2,["Moscow"])
print(travel_log)
#here we are testing how nesting works, and how to add new countries to a LIST of dictionaries















        