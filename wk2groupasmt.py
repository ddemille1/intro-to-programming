print('Please enter the following infomation:')
print()
first_name = input('First name: ')
last_name = input('Last name: ')
email = input('Email address: ')
phone_number = input('Phone number: ')
job_title = input('Job title: ')
id_number = input('ID number: ')
hair_color = input('Hair color: ')
eye_color = input('Eye color: ')
start_month = input('What month did you start: ')
advanced_training = input('Have you completed advanced training?(y/n): ')
print()
print('The ID Card is:')
print('-------------------------------------')
#faster, shorter code for line 18
#print(f'{last_name.upper()}, {first_name.capitalize()}' )
print(last_name.upper() + ', ' + first_name.capitalize())
print(job_title.title())
print('ID: ' + id_number)
print()
print(email.lower())
print(phone_number)
print()
print('Hair:  {0:25} Eyes:     {1}'.format(hair_color, eye_color))
print('Month: {0:25} Training: {1}'.format(start_month,advanced_training))
#print(hair_color + eye_color)
#print(start_month + advanced_training)
print('-------------------------------------')