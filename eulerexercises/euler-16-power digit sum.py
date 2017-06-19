import time
def power2sum(exp):
    powstr = str(2**exp)
    return sum(int(i) for i in powstr)


if __name__ == "__main__":
    start = time.time()
    solution = power2sum(1000)
    elapsed = time.time() - start
    print("Solution {} is found for {} seconds".format(str(solution), elapsed))