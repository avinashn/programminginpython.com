__author__ = 'Avinash'

lst = []
num = int(input("Enter size of list 1:"))
for n in range(num):
    numbers = int(input("Enter any number"))
    lst.append(numbers)

lst2 = []
num2 = int(input("Enter size of list 2:"))
for n in range(num2):
    numbers2 = int(input("Enter any number"))
    lst.append(numbers2)

merged_lists = lst + lst2

print("Merged list: ", merged_lists)
