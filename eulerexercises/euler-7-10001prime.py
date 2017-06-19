from math import ceil
import time
def is_prime(n):
    top = int(ceil(n**0.5))
    for i in range(3, top+1, 2):
        if n % i == 0:
            return False
    return True




def primes(max):
    yield 2
    found =1
    current = 3
    while found < max:
        if is_prime(current):
            yield current
            found+=1
        current +=2

if __name__ == "__main__":
   start = time.time()
   max = 1
   for prime in primes(10001):
       if int(prime)> max:
           max = prime
   elapsed = time.time() - start
   print("Solution {} is found for {} seconds".format(str(max), elapsed))