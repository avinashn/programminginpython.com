__author__ = 'Avinash'


# Python3 program to print alphabet pattern G

#   * * * * * *
# *
# *
# *     * * * * *
# *             *
# *             *
# *             *
#   * * * * * *

def print_pattern(n):
    # Outer for loop for number of rows
    for rows in range(n):

        # Inner for loop columns
        for columns in range(n):

            # prints first row
            if ((rows == 0 and (columns != 0 and columns != n-1)) or
               # prints last row
                (rows == n - 1 and (columns != 0 and columns != n-1)) or
                # prints first column
                ((columns == 0 and (rows != 0 and rows != n-1)) or
                 # prints last column
                 (columns == n-1 and rows != n-1 and rows >= (n/2)-1)) or
                # prints middle column
                (rows == (n/2)-1 and ((n/2)-1 <= columns < n-1))
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
