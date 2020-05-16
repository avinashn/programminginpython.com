__author__ = 'Avinash'


# Python3 program to count vowels in a string

# string of vowels
vowels = 'aeiou'

input_str = input("Enter a string: ")

# make input string case insensitive
input_str = input_str.casefold()

# make a dictionary with each vowel a key and value 0
vowels_count = {}.fromkeys(vowels, 0)

# count the number of each vowels
for letter in input_str:
    if letter in vowels_count:
        vowels_count[letter] += 1

print(vowels_count)
