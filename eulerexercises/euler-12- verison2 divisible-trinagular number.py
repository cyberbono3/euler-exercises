import time
#1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
from math import ceil
def generate_triangles(limit):
    l =1
    while l < limit:
        yield sum(range(l+1))
        l += 1

def get_factor(n):
    top = int(ceil(n** 0.5))+ 1
    return sum (2 for i in (2,top) if not n % i) # divisible without remainder

if __name__ == "__main__":
   start = time.time()
   for triangle in generate_triangles(99999999):
       if get_factor(triangle) > 499:
           solution = triangle
           break
   elapsed = time.time() - start
   print("Solution {} is found for {} seconds".format(str(solution), elapsed))
