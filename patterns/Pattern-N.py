__author__ = 'Avinash'


# Python3 program to print alphabet pattern N

# *             *
# * *           *
# *   *         *
# *     *       *
# *       *     *
# *         *   *
# *           * *
# *             *

def print_pattern(n):
    for row in range(n):
        for column in range(n):
            # first column
            if ((column == 0 or

                 # last column
                 column == n - 1) or

                # slanting line
                row == column
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
