with open('life-expectancy.csv') as life_expectancy_file:
    life_expectancy_list = []
    list_with_diff = []

    for line in life_expectancy_file:
        life_expectancy_file = line.strip()
        parts = line.split(',')
        country = parts[0]
        year = int(parts[2])
        life_expectancy = float(parts[3])

        
        life_expectancy_list.append(int(life_expectancy))
        for n in range(1, len(life_expectancy_list)):
            list_with_diff.append(life_expectancy_list[n]-life_expectancy_list[n-1])
    biggest_diff = max(list_with_diff)
    print(f'The biggest change between years is: {biggest_diff}')
       
#len(life_expectancy_list