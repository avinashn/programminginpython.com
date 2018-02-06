__author__ = 'Avinash'

input_num = (input("Enter any number: "))

try:
    arm_num = 0
    val = int(input_num)
    while val > 0:
        reminder = val % 10
        arm_num += reminder ** 3
        val //= 10

    if int(input_num) == arm_num:
        print(input_num, 'is an ARMSTRONG number')
    else:
        print(input_num, 'is NOT an armstrong number')

except ValueError:
    print("That's not a valid number, Try Again !")
