__author__ = 'Avinash'

size = int(input("Enter the range: \t "))
k = 1

for i in range(1, size + 1):
    for j in range(1, i + 1):
        print(k, end=" ")
        k = k + 1
    print("\n")

for i in range(1, size + 1):
    for j in range(1, i + 1):
        print('*', end=" ")
    print("\n")
