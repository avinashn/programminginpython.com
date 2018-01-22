__author__ = 'Avinash'

# set of all numbers from 1 to 10
numbers = set()

# set of all even numbers between 1 to 10
even_numbers = set()

# set of all odd numbers between 1 to 10
odd_numbers = set()

# set of all prime numbers between 1 to 10
prime_numbers = set()

# set of all composite numbers between 1 to 10
composite_numbers = set()


# function which finds even and odd numbers
def even_odd_sets(num):
    if num % 2 == 0:
        even_numbers.add(num)
    else:
        odd_numbers.add(num)


# function which finds prime and composite numbers
def prime_composite_sets(num):
    if num > 1:
        for j in range(2, num):
            if (num % j) == 0:
                composite_numbers.add(num)
                break
        else:
            prime_numbers.add(num)


for i in range(1, 11):
    numbers.add(i)

    even_odd_sets(i)

    prime_composite_sets(i)


print("\nNumbers Set: ", numbers)
print("Even Numbers Set: ", even_numbers)
print("Odd Numbers Set: ", odd_numbers)
print("Prime Numbers Set: ", prime_numbers)
print("Composite Numbers Set: ", composite_numbers)

# SET OPERATIONS

# Length of the set
print("\n\nLength of set numbers:",
      len(numbers))

# Intersection of sets
print("Intersection of numbers and even_numbers:",
      numbers.intersection(even_numbers))

# Union of sets
print("Union of prime_numbers and composite_numbers:",
      prime_numbers.union(composite_numbers))

# Difference of sets
print("Difference between numbers and prime_numbers:",
      numbers-prime_numbers)


example = set(['test', 43, 'another', 120])
print("\nExample Set:", example)

# Remove element in a set
example.remove(120)
print(example)

example.discard(43)
print(example)

# Clear the set
example.clear()
print(example)

