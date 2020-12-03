
#country 0, code 1, year 2, life expectancy 3, 
with open('life-expectancy.csv') as life_expectancy_file:
    shortest_life = 200
    longest_life = -1
    shortest_country = ""
    longest_country = ""
    shortest_year = ""
    longest_year = ""

    user_selected_year = int(input("What year would you like to know about? "))
    avg_life_expectancy_list = []
    user_shortest_life = 200 
    user_shortest_country = ""

    user_longest_life = -1
    user_longest_country = ""

    #info about a specific country
    user_selected_country = input("What country would you like to know about? ")
    avg_life_expectancy_list_by_country = []
    user_shortest_life_by_country = 200
    user_shortest_year_by_country = ""
    user_longest_life_by_country = -1
    user_longest_year_by_country = ""


    for line in life_expectancy_file:
        life_expectancy_file = line.strip()
        parts = line.split(',')
        country = parts[0]
        year = int(parts[2])
        life_expectancy = float(parts[3])
        if life_expectancy < shortest_life:
            shortest_life = life_expectancy   
            shortest_country = country    
            shortest_year = year
        if life_expectancy > longest_life:
            longest_life = life_expectancy
            longest_country = country
            longest_year = year

 #avg life expectancy for user selected year:         
        if user_selected_year == year:
            #make list of life expectancies for each year that matches user selected year,
            avg_life_expectancy_list.append(life_expectancy)
#find country with lowest life expectancy for the user selected year
            if life_expectancy < user_shortest_life:
                user_shortest_life = life_expectancy   
                user_shortest_country = country    
            if life_expectancy > user_longest_life:
                user_longest_life = life_expectancy
                user_longest_country = country

#gather infor about a specific country of user's choice
        if user_selected_country.lower() == country:
            avg_life_expectancy_list_by_country.append(life_expectancy)
            if life_expectancy < user_shortest_life_by_country:
                user_shortest_life_by_country = life_expectancy   
                user_shortest_year_by_country = year    
            if life_expectancy > user_longest_life_by_country:
                user_longest_life_by_country = life_expectancy
                user_longest_year_by_country = year
            print(avg_life_expectancy_list_by_country)            
    print(f'The longest life expectancy in {user_selected_country} is {user_longest_life_by_country}. It occured in {user_longest_year_by_country}.')
    print(f'The shortest life expeceancy in {user_selected_country} is {user_shortest_life_by_country}. It occured in {user_shortest_year_by_country}.')

#add years in the list together,
    sum = sum(avg_life_expectancy_list)
#count the number of items in the list.
    number_of_years = len(avg_life_expectancy_list)
#divide sum/number to get avg
    avg_life_expectancy = sum/number_of_years


    print(f'\nThe average life expectancy in {user_selected_year} was: {avg_life_expectancy:.2f}.')
    print(f'The longest life expectancy in {user_selected_year} was: {user_longest_life} in {user_longest_country}.')
    print(f'The shortest life expeceancy in {user_selected_year} was: {user_shortest_life} in {user_shortest_country}.\n')
    

    print(f'The shortest life expectancy of the data set is: {shortest_life} in {shortest_country} in {shortest_year}.')
    print(f'The longest life expectancy of the data set is: {longest_life} in {longest_country} in {longest_year}.')


