__author__ = 'Avinash'

# Print a Triangle

# Range of the triangle
num = int(input("Enter the range: \t "))

# i loop for range(height) of the triangle
# first j loop for printing space ' '
# second j loop for printing stars '*'
for i in range(num):
    for j in range((num - i) - 1):
        print(end=" ")
    for j in range(i + 1):
        print("*", end=" ")
    print()
