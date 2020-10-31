__author__ = 'Avinash'


# Python3 program to print alphabet pattern K

# *           *
# *         *
# *       *
# *     *
# *   *
# * *
# *   *
# *     *
# *       *
# *         *
# *           *
# *             *


def print_pattern(n):

    i = 0
    j = n//2
    # Outer for loop for number of rows
    for rows in range(n):

        # Inner for loop columns
        for columns in range(n):

            # prints first and last column
            if columns == 0 or (rows == (columns+(n//3)) and columns > 0):
                print("*", end=" ")
            elif rows == i and columns == j:
                print("*", end=" ")
                i = i+1
                j = j-1
            else:
                print(" ", end=" ")
        print()


size = int(input("Enter size: \t"))

if size < 8:
    print("Enter a size greater than 8")
else:
    print_pattern(size)
