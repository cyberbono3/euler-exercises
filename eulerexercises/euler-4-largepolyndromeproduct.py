from math import ceil
def is_palindrome(num):
    s = str(num)
    '90109'
    s1 = s[0: int(len(s) / 2)]
    s2 = s[int(ceil(len(s)/ 2.0)):]
    return s1 == s2[::-1]

def find_largest_palindrome(min, max):
    result = 0
    for x in range(min, max):
        for y in range(min, max):
             z = x * y
             if is_palindrome(z) and z > result:
                 result = z

    return result



def main():

        solution = find_largest_palindrome(100,1000)
        print("The largest palindrome: " + str(solution))

if __name__ == "__main__":
	main()