import numpy as np

# Create an array of integers from 0 to 9
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Create a range of values from 0 to 9 with a step of 2
range_arr = np.arange(0, 10, 2)
print('The range of values from 0 to 9 with a step of 2: \t', range_arr)

# Create an array of zeros with 3 rows and 4 columns
zeros_arr = np.zeros((3, 4))
print('An array of zeros with 3 rows and 4 columns: \t', zeros_arr)

# Create an array of ones with 2 rows and 3 columns
ones_arr = np.ones((2, 3))
print('An array of ones with 2 rows and 3 columns: \t', ones_arr)

# Create an array with 5 evenly spaced values between 0 and 1
linspace_arr = np.linspace(0, 1, 5)
print('An array with 5 evenly spaced values between 0 and 1: \t', linspace_arr)

# Create an array of 5 random values between 0 and 1
rand_arr = np.random.rand(5)
print('An array of 5 random values between 0 and 1: \t', rand_arr)

# Find the maximum value in the array
max_val = np.max(arr)
print('Maximum value in the array: \t', max_val)

# Find the minimum value in the array
min_val = np.min(arr)
print('Minimum value in the array: \t', min_val)

# Find the mean value of the array
mean_val = np.mean(arr)
print('Mean value of the array: \t', mean_val)

# Find the standard deviation of the array
std_val = np.std(arr)
print('Standard deviation of the array: \t', std_val)
