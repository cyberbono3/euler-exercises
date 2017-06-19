import time
from num2words import num2words



def number_letter_count(num):
    return sum (1 for l in num2words(num) if l.isalpha())






if __name__ == "__main__":
    start = time.time()
    count = 0
    for i in range (1,1001):
        count += number_letter_count(i)
    solution = count
    elapsed = time.time() - start
    print("Solution {} is found for {} seconds".format(str(solution), elapsed))


