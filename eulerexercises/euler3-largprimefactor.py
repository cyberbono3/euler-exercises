from math import floor
"""lets code"""

def factor(num):
    if num != 2 and num % 2 == 0:
        result = [2]
    others = [i for i in range(3, int(floor(num **0.5)),2) if (num % i == 0 and len(factor(i))== 0)]
  """  for i in range(3, int(floor(num **0.5)),2):
        if num % i == 0:
            if len(factor(i))== 0:
                result.append(i)"""



def main():
	try:
	    result = factor(606341371901192354470259703076328716992246317693812238045286463)
	    print("The divisors list  is "+ str(result))
	    maxdiv = result[-1]
	    print("The largest prime divisor is " + str(maxdiv))


	except (ValueError, TypeError, StopIteration) as e:
	    print ('Exception is handled{}'.format(str(e)))



if __name__ == "__main__":
	main()

