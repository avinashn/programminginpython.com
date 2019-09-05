__author__ = 'Avinash'

# Python3 program to print alphabet B pattern

# Function to display alphabet pattern


def print_pattern(n):
    # Outer for loop for number of lines(rows)
    for i in range(n):

        # Inner for loop for logic execution
        for j in range(n + 1):

            # prints two column lines
            if ((j == 0 or j == n) or

                    # print first line of alphabet
                    i == 0 and j != 0 and j != n or

                    # prints last line
                    i == n - 1 or

                    # prints middle line
                    i == n // 2):
                print("*", end="")
            else:
                print(" ", end="")

        print()


# Size of the letter
num = int(input("Enter the size: \t "))

if num > 7:
    print_pattern(num)
else:
    print("Enter a size minimum of 8")
