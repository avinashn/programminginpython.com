__author__ = 'Avinash'


# Python3 program to print alphabet pattern H

# *         *
# *         *
# *         *
# * * * * * *
# *         *
# *         *
# *         *


def print_pattern(n):
    # Outer for loop for number of rows
    for rows in range(n):

        # Inner for loop columns
        for columns in range(n):

            # prints first and last column
            if ((columns == 0 or columns == n-1) or
               # prints middle row
                (rows == n // 2)
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
