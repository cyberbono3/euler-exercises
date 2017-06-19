import time
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def factorial_digit_sum(num):
    fac = factorial(num)
    return sum(int(i) for i in str(fac))



if __name__ == "__main__":
    start = time.time()
    solution = factorial_digit_sum(100)
    elapsed = time.time() - start
    print("Solution {} is found for {} seconds".format(str(solution), elapsed))

"""
first means
from math import factorial
factorial_100 -factorial(100)
return sum(int(i) for i in str(factorial_100))


second means
stringified= str(factorial_100)
digits = []
for character in stringfied:
integer= int(character)
digits.append(integer)

digits = (int(c) for c in stringified)



"""

