# data set comes in this order:
# country 0, code 1, year 2, life expectancy 3

# Import statistics module for later calculations.
import statistics

# Open the file save it to variable named life_expectancy_file. 
# Define variables that will be used later for finding shortest, longest life expectancy and identifying which country and year they occurd in.
with open('life-expectancy.csv') as life_expectancy_file:
    shortest_life = 200
    longest_life = -1
    shortest_country = ""
    longest_country = ""
    shortest_year = ""
    longest_year = ""

# Ask user for year from which to pull data.
# Set up list to contain all the values for the year the user selected.
# Define variables for shortest, longest life expectancies in user selected year and identifying which countries they occured in. 
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

# Iterate through each line of the file.
# Splitting it into a list named parts. 
# Naming variables for the cleaned data we're interest in.
    for line in life_expectancy_file:
        parts = line.split(",")
        country = parts[0].strip()
        year = int(parts[2])
        life_expectancy = float(parts[3].strip())

# Finding the shortest life expectancy of the dataset and identifying which country and year it occured in.
        if life_expectancy < shortest_life:
            shortest_life = life_expectancy   
            shortest_country = country    
            shortest_year = year

# Finding the longest life expectancy of the dataset and identifying which country and year it occured it.
        if life_expectancy > longest_life:
            longest_life = life_expectancy
            longest_country = country
            longest_year = year

# Finding the avg life expectancy for the year selected by the user
# Making list called "avg_life_expectancy_list" containing all the life expectancies for the year the user selected         
        if user_selected_year == year:
            avg_life_expectancy_list.append(life_expectancy)

# Finding lowest life expectancy and associated country for the user selected year
            if life_expectancy < user_shortest_life:
                user_shortest_life = life_expectancy   
                user_shortest_country = country    

# Finding highest life expectancy and associated coutry for the user selected year
            if life_expectancy > user_longest_life:
                user_longest_life = life_expectancy
                user_longest_country = country

# Gather infor about a specific country of user's choice
        if user_selected_country.lower() == country.lower():
            avg_life_expectancy_list_by_country.append(life_expectancy)
            if life_expectancy < user_shortest_life_by_country:
                user_shortest_life_by_country = life_expectancy   
                user_shortest_year_by_country = year    
            if life_expectancy > user_longest_life_by_country:
                user_longest_life_by_country = life_expectancy
                user_longest_year_by_country = year         

# Code to calculate the avg life expectancy for the user selected year.
    avg_life_expectancy = statistics.mean(avg_life_expectancy_list)

#code to calculate the avg life expectancy for the user selected country.
    country_life_expectancy= statistics.mean(avg_life_expectancy_list_by_country)

# Printing results for the user's selected year.
    print(f'\nThe average life expectancy in {user_selected_year} was: {avg_life_expectancy:.2f} years.')
    print(f'The longest life expectancy in {user_selected_year} was: {user_longest_life:.2f} years. It occured in {user_longest_country}.')
    print(f'The shortest life expeceancy in {user_selected_year} was: {user_shortest_life:.2f} years. It occured in {user_shortest_country}.\n')

# Print longest life expectancy and in which year it occured for user selected country. chosen by user
    print(f'\nThe average life expectancy in {user_selected_country} is {country_life_expectancy:.2f} years.')
    print(f'The longest life expectancy in {user_selected_country} is {user_longest_life_by_country:.2f} years. It occured in {user_longest_year_by_country}.')
    print(f'The shortest life expeceancy in {user_selected_country} is {user_shortest_life_by_country:.2f} years. It occured in {user_shortest_year_by_country}.\n')


#printing results for the entire data set.
    print(f'The longest life expectancy of the data set is: {longest_life:.2f} years in {longest_country} in {longest_year}.')
    print(f'The shortest life expectancy of the data set is: {shortest_life:.2f} years in {shortest_country} in {shortest_year}.')
    

