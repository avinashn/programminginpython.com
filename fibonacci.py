__author__ = 'Avinash'


def fibonacci(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


number = int(input("Enter an integer: \t"))
for i in range(number):
    print(fibonacci(i))
