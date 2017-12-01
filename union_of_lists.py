__author__ = 'Avinash'

lst = []
num = int(input("Enter size of list 1: \t"))
for n in range(num):
    numbers = int(input("Enter any number: \t"))
    lst.append(numbers)

lst2 = []
num2 = int(input("Enter size of list 2: \t"))
for n in range(num2):
    numbers2 = int(input("Enter any number: \t"))
    lst2.append(numbers2)

union = list(set().union(lst, lst2))
print("\nThe Union of two lists is \t", union)
