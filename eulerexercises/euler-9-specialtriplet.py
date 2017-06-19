'''
a + b = c = 1000
a**2 + b**2 = c**2

'''

import time
def calproduct(max):
    for a in range(1,max+1):
        for b in range(1,max+1):
            if a>b:
                continue
            if a + b + (a**2 + b**2)**0.5 == max:
                c = int((a**2 + b**2)**0.5)
                print ("a: " + str(a)+ " b: " + str(b) + " c: " + str(c))
                product = a*b*c
    return product


if __name__ == "__main__":
   start = time.time()
   solution = calproduct(1000)
   elapsed = time.time() - start
   print("Solution {} is found for {} seconds".format(str(solution), elapsed))