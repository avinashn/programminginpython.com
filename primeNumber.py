__author__ = 'Avinash'

num = int(input("Enter any number : "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is NOT a prime number")
            break
    else:
        print(num, "is a PRIME number")
elif num == 0 or 1:
    print(num, "is a neither prime NOR composite number")
else:
    print(num, "is NOT a prime number it is a COMPOSITE number")
