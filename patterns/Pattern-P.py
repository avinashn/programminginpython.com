__author__ = 'Avinash'


# Python3 program to print alphabet pattern P

#   * * * * * * * * * *
# *                     *
# *                     *
# *                     *
# *                     *
# *                     *
# * * * * * * * * * * *
# *
# *
# *
# *

def print_pattern(n):
    for row in range(n):
        for column in range(n):
            if (

              # first row
              (row == 0 and (column != 0 and column != n-1)) or

              # middle row
              (row == n//2 and column != n-1) or

              # first column
              (column == 0 and (row !=0 and row != n-1)) or

              # last column
              (column == n-1 and row < n//2 and row != 0)
            ):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


size = int(input("Enter a size:\t"))

if size < 8:
    print("Enter a size minumin of 8")
else:
    print_pattern(size)

