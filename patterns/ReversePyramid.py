__author__ = 'Avinash'

# Print a Reverse Pyramid

# Range of the Reverse Pyramid
num = int(input("Enter the range: \t "))

for rows in range(num, 0, -1):
    for columns in range(0, num-rows):
        print(end=" ")
    for columns in range(0, rows):
        print("*", end=" ")
    print()
