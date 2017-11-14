__author__ = 'Avinash'

# add elements to dictionary
my_info = {
    'Name': 'Avinash',
    'Age': 23,
    'Gender': 'Male',
    'Location': 'India',
    'Website': 'programminginpython.com'
    }

# print dictionary
print(my_info)

# print value of a key
print(my_info['Name'])

# modify elements in dictionary
my_info['Age'] = 24
print(my_info)

# length of dictionary
print(len(my_info))

# delete a particular key
del my_info['Website']
print(my_info)

# removes all elements in dictionary
my_info.clear()
print(my_info)

# delete entire dictionary
del my_info
