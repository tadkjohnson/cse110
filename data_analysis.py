


high_expectancy = float("1")
high_country = "Pluto"
high_year = 0

lowest_life_expectancy = float("100")
lowest_country = "Mars"
lowest_year = 0


# total_expect = 10
# count = 0
# min_expect = float("0:.4f")
# max_expect = float("0:.4f")
# min_place = "Moon"
# max_place = "Sun"

#  using a list to do it 
user_year_list = []

user_year = int(input("give me a year you would like information from "))

with open("life-expectancy.csv") as flu_input:    #opens txt file and gives it a new name  does this look up 1 level for the file?
    next(flu_input)    #skips the first line whicch is the header line

    for line in flu_input:  #start to loop 
        flu_list = line.split(",")   #seperates the line of information at the space 
        entity = flu_list[0] #assigns first item in list is the name
        code = (flu_list[1])
        year = int(flu_list[2])
        life_expect = float(flu_list[3])

        if life_expect < lowest_life_expectancy:  #lowest life expectance
            lowest_expectancy = life_expect
            lowest_country = entity
            lowest_year = year

        if life_expect > high_expectancy:  #highest life expectations
            high_expectancy = life_expect
            high_country = entity
            high_year = year

        if year == user_year:
            user_year_list.append((life_expect))
       
            
if user_year_list:
    total = sum(user_year_list)
    avg_life = total / len(user_year_list)
    max_expect = max(user_year_list)
    min_expect = min(user_year_list)
    print(f"{max_expect} {min_expect}")
    # max_place = [entity]
    # min_place = [entity]

    for life in user_year_list:
        total += life

    if life_expect > max_expect:
        max_expect = life_expect
        
    if life_expect < min_expect:
        min_expect = life_expect
        
        print (f"In the year you choose {user_year}, the average life span was {avg_life:.3f}, the longest life was {max_expect:.3f}, and the shortest was {min_expect:.3f}")

    # else:
    #     print("No data found, sorry")        



# print (f"{user_year_list}")
# print (f"{total}")
 
# print (f"{max_expect}")
# print (f"{min_expect}")
# print (f"{avg_life}")
# print (f"{max_place}")
# print (f"{max_place}")

print (f"In the year you choose {user_year}, the average life span was {avg_life:.3f}, the longest life was {max_expect:.3f}, and the shortest was {min_expect:.3f}")


# this below jsut are print statements for original questions
print()
print(f"The overall lowest life expectancy was {lowest_expectancy:.3f} in {lowest_country} in {lowest_year}")
print(f"The overall highest life expectancy was {high_expectancy:.3f} in {high_country} in {high_year}")






 







