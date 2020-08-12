__author__ = 'Avinash'

# Python3 program to print alphabet F pattern

# *********
# *
# *
# *
# *********
# *
# *
# *


def print_pattern(n):
    # Outer for loop for number of rows
    for row in range(n):

        # Inner for loop columns
        for column in range(n):

            # prints first and middle row
            if ((row == 0 or row == n // 2) or

                    # prints first column
                    column == 0):
                print("*", end="")
            else:
                print(" ", end="")
        print()


size = int(input("Enter size: \t"))

if size < 8:
    print("Enter a size greater than 8")
else:
    print_pattern(size)
