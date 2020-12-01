with open("hr_system.txt") as employees:
    for line in employees:
        employees = line.strip()
        part = line.split(",")
​
        name = part[0]
        number = part[1]
        title = part[2]
        salary = float(part[3])
        paycheck = float(salary/24)
​
        if title.lower() == "engineer":
           paycheck += 1000
​
        print(f' Name: {name} (ID: {number}), {title} - ${paycheck:.2f}')
​
