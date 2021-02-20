__author__ = 'Avinash'


# Python3 program to print alphabet pattern W

# *                           *
# *                           *
# *                           *
# *                           *
# *                           *
# *                           *
# *                           *
# *             *             *
# *           *   *           *
# *         *       *         *
# *       *           *       *
# *     *               *     *
# *   *                   *   *
# * *                       * *
# *                           *

def print_pattern(n):
    for row in range(n):
        for column in range(n):
            if(
                    # first column
                    (column == 0) or

                    # last column
                    (column == n-1) or

                    # left slanting line
                    (row+column == n-1 and row >= n//2) or

                    # right slanting line
                    (row == column and row >= n//2)
            ):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


size = int(input("Enter any size: \t"))

if size < 8:
    print("Enter a number minimum of 8")
else:
    print_pattern(size)
