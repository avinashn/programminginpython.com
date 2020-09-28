__author__ = 'Avinash'

input_num = int(input('Enter any number: '))

if input_num % 2 == 0:
    print(input_num, "is EVEN")
else:
    print(input_num, "is ODD")

##### Another Way with Function #####

def even_odd(input_num): # defining function
    if input_num % 2 == 0:
        print(input_num, "is EVEN")
    else:
        print(input_num, "is ODD")
        
input_num = int(input('Enter any number: '))
even_odd(input_num) # calling function
