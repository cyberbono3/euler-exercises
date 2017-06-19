# 1)find the divisors of n
# 2)If d(a) = b and d(b) = a,
# where a ≠ b,
# then a and b are an amicable pair and
# each of a and b are called amicable numbers.
# 3) calculate sum of all amicable numbers under 100000

import time
from math import ceil

def d(n):
    result = sum(int(i) for i in range(1,n) if n % i == 0 )
    return result



#caklculateall ds under 10000

def ds(max):
    return [(i, d(i)) for i in range(1, max)
            if d(d(i)) == i and d(i)!=i and d(i) < max]
data = ds(10000)
print ('data' + str(data))
numbers = []
for i,d in data:
     numbers = [j for (j,e) in data]
print("numbers " + str(numbers))
print("sum of numbers " + str(sum(numbers)))












"""
def ds(max):
     return [(i, d(i)) for i in range(1,max)]
           #returned list of tuples
          #  if d(d(i)) == i and d(i)!=i and d(i) < max]
data = ds(285)
numbers = []
for (i, d) in data:
    p = [j for (j,e) in data if e == i ]
    print ( str(i) + "  " + str(d) + "  " + str(p))
    numbers += p
print(" List of numbers is: " + str(numbers))
s = set(numbers)
print(" set of numbers is: " + str(s))
print("Sum of numbers set: " + str(sum(s)))

"""


'''
if __name__ == "__main__":
    start = time.time()
    solution = ds(10000)
    elapsed = time.time() - start
    print("Solution {} is found for {} seconds".format(str(solution), elapsed))'''
