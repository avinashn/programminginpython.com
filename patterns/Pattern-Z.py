__author__ = 'Avinash'

# Python3 program to print alphabet pattern Z

'''
    * * * * * * * * 
                *   
              *     
            *       
          *         
        *           
      *             
    * * * * * * * * 
'''


def print_pattern(n):
    for row in range(n):
        for column in range(n):
            if(
                    # first row
                    (row == 0) or

                    # last row
                    (row == n-1) or

                    # slanting line
                    (row+column == n-1)
            ):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


size = int(input("Enter any size: \t"))

if size < 8:
    print("Enter a size minimum of 8")
else:
    print_pattern(size)
