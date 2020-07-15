__author__ = 'Avinash'


# Python3 program to print alphabet pattern D

# * * * * *
# *         *
# *         *
# *         *
# *         *
# *         *
# *         *
# * * * * *

def print_pattern(n):
  # Outer for loop for number of rows
  for row in range(n):

    # Inner for loop columns
    for column in range(n - 2):

      # prints first and last row
      if (
        ((row == 0 or row == n-1) and (0 < column < n-3)) or

        # prints first column
        column == 0 or

        # prints last column
        column == n - 3 and (row != 0 and row != n - 1)
      ):
        print("*", end=" ")
      else:
        print("  ", end="")
    print()

# Size of the letter
num = int(input("Enter the size \t"))

if num < 8:
  print("Enter a number atleast 8")
else:
  print_pattern(num)
