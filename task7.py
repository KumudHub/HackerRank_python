#The included code stub will read an integer, , from STDIN.

#Without using any string methods, try to print the following:
# 123....n

#Note that "...." represents the consecutive values in between.


def printf(n):
        
        for i in range(1,n+1):
            print(i, end="")    # to print the numbers in a single line


printf(5)