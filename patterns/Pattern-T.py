__author__ = 'Avinash'


# Python3 program to print alphabet pattern T

'''
* * * * * * * * * 
        *         
        *         
        *         
        *         
        *         
        *         
        *         
        *       
'''


def print_pattern(n):
    for row in range(n):
        for column in range(n):
            if (
                    # first row
                    (row == 0) or

                    # middle column
                    (column == n//2)
            ):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


size = int(input("Enter a size: \t"))

if size < 8:
    print("Enter a size minimum of 8")
else:
    print_pattern(size)
