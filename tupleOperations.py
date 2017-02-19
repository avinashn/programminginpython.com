__author__ = 'Avinash'

tup = ('abc', 'def', 'ghi', 'jklm', 'nopqr', 'st', 'uv', 'wxyz', '23', 's98', '123', '87')

# prints the length of the tuple
print('\ntuple: ', tup)
print('Length of the tuple is : ', len(tup))

# Slicing
# shows only items starting from 0 upto 3
print('\ntuple: ', tup)
print('tuple showing only items starting from 0 upto 3\n', tup[:3])

# shows only items starting from 4 to the end
print('\ntuple: ', tup)
print('tuple showing only items starting from 4 to the end\n', tup[4:])

# shows only items starting from 2 upto 6
print('\ntuple: ', tup)
print('tuple showing only items starting from 2 upto 6\n', tup[2:6])

# reverse all items in the tuple
print('\ntuple: ', tup)
print('tuple items reversed \n', tup[::-1])

# removing whole tuple
del tup

tup_0 = ("ere", "sad")
tup_1 = ("sd", "ds")
print('\nfirst tuple: ', tup_0)
print('second tuple: ', tup_1)
tup = tup_0 + tup_1
print('Concatenation of 2 tuples  \n', tup)
