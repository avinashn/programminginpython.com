__author__ = 'Avinash'


def bubble_sort(sort_list):
    for j in range(len(sort_list)):
        for k in range(len(sort_list) - 1):
            if sort_list[k] > sort_list[k + 1]:
                sort_list[k], sort_list[k + 1] = sort_list[k + 1], sort_list[k]
    print('\nThe sorted list: \t', sort_list)
    print('\n')


lst = []
size = int(input("\nEnter size of the list: \t"))

for i in range(size):
    elements = int(input("Enter the element: \t"))
    lst.append(elements)

bubble_sort(lst)
