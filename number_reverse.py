__author__ = 'Avinash'

input_num = (input("Enter any number: "))
reverse = 0
try:
    val = int(input_num)
    while val > 0:
        reminder = val % 10
        reverse = (reverse * 10) + reminder
        val //= 10
    print('Reverse of given number is : ', reverse)
except ValueError:
    print("That's not a valid number, Try Again !")
