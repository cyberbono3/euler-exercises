import time


def memoize(f):
    cache = {}

    def memoizer(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoizer


def count_collatz(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        n = n/2
        return 1 + count_collatz(n)
    n = 3*n +1
    return 1 + count_collatz(n)


def cal_longest_chain():
    max = 0
    for i in range(1,1000000):
        c = count_collatz(i)
        if c > max:
            max = c
            numbers = [i]
    return numbers





if __name__ == "__main__":
    start = time.time()
    solution = cal_longest_chain()
    elapsed = time.time() - start
    print("Solution {} is found for {} seconds".format(str(solution), elapsed))






'''
import time
# 1) generate sequence starting at 13 ending in 1
# 2) return number of the elemtns in the sequence
#3) which starting number under 1 million produces the longest chain?

def cal_collatz(t):
    count = 1
    while t > 1 :
        if t % 2 == 0:
            t = t/2
        else:
            t = 3*t + 1
        count+=1
    return count

def cal_longest_chain():
    max = 0
    numbers_list = []
    for i in range(14,1000000):
        c = cal_collatz(i)
        if c > max:
            max = c
            numbers_list.append(i)
    return numbers_list[-1]




if __name__ == "__main__":
    start = time.time()
    solution = cal_longest_chain()
    elapsed = time.time() - start
    print("Solution {} is found for {} seconds".format(str(solution), elapsed))
#Solution 837799 is found for 33.77993202209473 seconds
'''