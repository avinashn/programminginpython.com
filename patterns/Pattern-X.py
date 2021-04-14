__author__ = 'Avinash'


# Python3 program to print alphabet pattern X

# *               *
#   *           *
#     *       *
#       *   *
#         *
#       *   *
#     *       *
#   *           *
# *               *

def print_pattern(n):
    for row in range(n):
        for column in range(n):
            if(
                    # right slanting line
                    (row == column) or

                    # left slanting line
                    (row + column == n-1)
            ):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


size = int(input("Enter any size: \t"))

if size < 8:
    print("Enter a size greater than 8")
else:
    print_pattern(size)
