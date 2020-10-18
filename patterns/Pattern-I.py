__author__ = 'Avinash'


# Python3 program to print alphabet pattern I
'''
* * * * * * * * * 
        *         
        *         
        *         
        *         
        *         
        *         
        *         
* * * * * * * * * 
'''


def print_pattern(n):
    # Outer for loop for number of rows
    for rows in range(n):

        # Inner for loop columns
        for columns in range(n):

            # prints first and last row
            if ((rows == 0 or rows == n-1) or
               # prints middle column
                (columns == n // 2)
            ):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


size = int(input("Enter size: \t"))

if size < 8:
    print("Enter a size greater than 8")
else:
    print_pattern(size)
