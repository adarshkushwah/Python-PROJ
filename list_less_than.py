# This program is meant to simply print a list of numbers less than the one provided by the user from the given list.

print('The given list is --> [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]')
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

x = int(input('Enter a number from the given list and this will print a new list of numbers less than the one entered by you : '))

print([y for y in a if y<x])