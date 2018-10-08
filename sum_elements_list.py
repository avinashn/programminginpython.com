__author__ = 'Avinash'
__author1__ = 'ramlaxman'

lst = []
total = int(input('Total numbers in List: '))

for num in range(total):
    num = int(input('Enter number '))
    lst.append(num)

print("Sum of elements in given list is :", sum(lst))
