# To find the n-th Fibonacci Number using formula
from math import sqrt 
# import square-root method from math library
def nthFib(n):
    res = (((1+sqrt(5))**n)-((1-sqrt(5)))**n)/(2**n*sqrt(5))
    # compute the n-th fibonacci number
    print(int(res),'is',str(n)+'th fibonacci number')
    # format and print the number
    
# driver code
nthFib(12)

# This code is contributed by Kush Mehta
