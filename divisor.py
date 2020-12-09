# This program asks the user for a number and then prints out a list of all the divisors of that number.

print('\nThis program asks the user for a number and then prints out a list of all the divisors of that number.')

num = int(input('\nPlease enter a number for which you want to find all the divisors for : '))
print('\n')
for divisors in range(1,num+1):
    if(num%divisors==0):
        print(divisors)
print('\n')
