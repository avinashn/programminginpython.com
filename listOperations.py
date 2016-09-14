__author__ = 'Avinash'

lst = ['abc', 'def', 'ghi', 'jklm', 'nopqr', 'st', 'uv', 'wxyz', '23', 's98', '123', '87']

# prints the length of the list
print('Length of the list is : ', len(lst))

# appends an item to the list
lst.append('sdd')
print('\nThe list appended a new element "sdd" at the end \n', lst)

# changes the value of an item in a list
lst[0] = 'aaa'
print('\nThe value of the first element in the list is changed to "aaa" \n', lst)

# Slicing
# shows only items starting from 0 upto 3
print('\nList showing only items starting from 0 upto 3\n', lst[:3])

# shows only items starting from 4 to the end
print('\nList showing only items starting from 4 to the end\n', lst[4:])

# shows only items starting from 2 upto 6
print('\nList showing only items starting from 2 upto 6\n', lst[2:6])

# reverse all items in the list
print('\nList items reversed \n', lst[::-1])

# removing items from list
lst[:1] = []
print('\nFirst element is removed from the list \n', lst)

# removing whole list
lst[:] = []
print('\nComplete list removed \n', lst)
