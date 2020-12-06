print('Program : Even or Odd, multiple of 4 and if also divisible evenly by another number entered by the user...')

num1 = int(input('Please enter a number to check the even/odd nature : '))
num2 = int(input('Enter another number for checking the even divisibility : '))

check = num1%2

multiple_of_four = num1%4

divisible = num1%num2

if check == 0 and multiple_of_four == 0 and divisible == 0:
    print(f'The number {num1} is even, is the multiple of 4 and evenly divisible by {num2}.')
elif check == 0 and multiple_of_four != 0 and divisible == 0:
    print(f'The number {num1} is even and is not the multiple of 4 but is evenly divisible by {num2}.')
elif check != 0 and multiple_of_four == 0 and divisible == 0 :
    print(f'The number {num1} is odd and is the multiple of 4 but is evenly divisible by {num2}')
elif check == 0 and multiple_of_four == 0 and divisible != 0:
    print(f'The number {num1} is even, is the multiple of 4 but not evenly divisible by {num2}.')
elif check != 0 and multiple_of_four == 0 and divisible != 0:
    print(f'The number {num1} is odd, is the multiple of 4 but not evenly divisible by {num2}.')
elif check != 0 and multiple_of_four != 0 and divisible == 0:
    print(f'The number {num1} is odd, is not the multiple of 4 but is evenly divisible by {num2}.')
elif check == 0 and multiple_of_four != 0 and divisible != 0:
    print(f'The number {num1} is even, is not the multiple of 4 but is not evenly divisible by {num2}.')
else :
    print(f'The number {num1} is odd, is also not a multiple of 4 and also not evenly divisible by {num2}.')