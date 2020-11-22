__author__ = 'Avinash'


# Python3 program to print alphabet pattern M

# *               *
# * *           * *
# *   *       *   *
# *     *   *     *
# *       *       *
# *               *
# *               *
# *               *
# *               *


def print_pattern(n):
    for row in range(n):
        for column in range(n):
            # first column
            if ((column == 0 or

                    # last column
                    column == n-1) or

                    # right slanting line
                    row + column == (n - 1) and row < n/2 or

                    # left slanting line
                    row == column and row < n/2
            ):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


size = int(input("Enter the size: \t"))

if size < 8:
    print("Enter a value minumin of 8")
else:
    print_pattern(size)
