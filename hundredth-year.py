print('This program is meant to help you determine the year in which you will turn 100 years old.')

name = input('Please enter your name : ')
age = int(input('Please enter your age : '))
current_year = int(input('Please also enter the current year : '))

hundredth_year = current_year + (100-age)

print(f'Hi {name}, you will become a hundred years old in the year {hundredth_year}.')