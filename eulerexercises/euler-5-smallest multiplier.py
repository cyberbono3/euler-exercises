check_list = [11, 13, 14, 16, 17, 18, 19, 20]

def find_solution(step):
    for num in range(step, 999999999999):
        if all(num % n == 0 for n in check_list):
            return num
    return None


if __name__ == "__main__":
    solution = find_solution(20)
    if solution is None:
        print("No solution was found")
    else:
        print ("Solution is found: " + str(solution))











""" Youtube solution a bit slow """
'''    
r = [11, 13, 14, 16, 17, 18, 19, 20]
def divisible_by(num):
    for x in r:
        if num % x != 0:
            return False
    return True

def find_smallest_multiple():
    max = 1
    for x in range(2, 21):
        max *= x
    min = max
    for test in range(max, 20, -1):
        if divisible_by(test):
            min = test
            print ('min:' + str(min))

    return min

def main():
    find_smallest_multiple()

if __name__ == "__main__":
    main()
'''