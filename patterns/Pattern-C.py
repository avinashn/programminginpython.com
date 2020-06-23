__author__ = 'Avinash'

# Python3 program to print alphabet pattern C

#  *********
# *
# *
# *
# *
# *
# *
#  *********


def print_pattern(n):
    # Outer for loop for number of lines(rows)
    for i in range(n):

        # Inner for loop for logic execution
        for j in range(n + 3):

            # Print 1st line
            if ((i == 0 or

                 # Print last line
                 i == n - 1) and

                    # For more reasonable curve
                    j > 0 or

                    # First column
                    (j == 0 and (i != 0 and i != n - 1))):
                print("*", end="")
            else:
                print(" ", end="")
        print()


num = int(input("Enter size: \t"))

if num > 7:
    print_pattern(num)
else:
    print("Enter a size minimum of 8")