__author__ = 'Avinash'


# Python3 program to print alphabet pattern S

#   * * * * * * *
# *
# *
# *
#   * * * * * * *
#                 *
#                 *
#                 *
#   * * * * * * *


def print_pattern(n):
    for row in range(n):
        for column in range(n):
            if (
                    # first row
                    (row == 0 and column != 0 and column != n - 1) or

                    # first column
                    (column == 0 and row != 0 and row < n//2) or

                    # middle row
                    (row == n//2 and column != n-1 and column != 0) or

                    # last column
                    (column == n-1 and row > n//2 and row != n-1) or

                    # last row
                    (row == n-1 and column != 0 and column != n - 1)
            ):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


size = int(input("Enter any size: \t"))

if size < 8:
    print("Enter a size minimum of 8")
else:
    print_pattern(size)

