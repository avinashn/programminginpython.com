__author__ = 'Avinash'

input_num = int(input("Enter any number: "))

count = 0
while input_num > 0:
    count += 1
    input_num //= 10
print("The number of digits in the given number are:", count)