__author__ = 'Avinash'

num = input('Enter any number : ')

try:
    val = int(num)
    print('Reverse of the given number is : ', str(num)[::-1])
except ValueError:
    print("That's not a valid number, Try Again !")
