__author__ = 'Avinash'


# Python3 program to print alphabet pattern V

# *                                   *
#   *                               *
#     *                           *
#       *                       *
#         *                   *
#           *               *
#             *           *
#               *       *
#                 *   *
#                   *

def print_pattern(n):
    # row looping
    for row in range(n):

        # column looping
        for column in range(n):
            if (
                    # right slanting line
                    (row + column == n - 1 and row < n / 2) or

                    # left slanting line
                    (row == column and row < n / 2)
            ):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


size = int(input("Enter any size: \t"))

if size < 8:
    print("Enter a size minimum of 8")
else:
    print_pattern((size * 2) + 1)
