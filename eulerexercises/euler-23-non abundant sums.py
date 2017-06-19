#  abundant number is number the sum of divisors exceeds the number
# all integers grater tan 28123 can be written  as the sum of 2 abundant numbers
# find th sum of al positiive integers which can not be written as the sum of two abundant numbers
# write the function that checks if numbers are
# generator comprehension of sum of the numbes that are not abundandant


# 1) lsit of all abundant numbers


#sum of divisors
def divisors_sum(n):
    result = sum(int(i) for i in range(1, n) if n % i == 0)
    return result

def is_abundant(n):
    return divisors_sum(n)>n
x=100
abundant_numbers = [int(i) for i in range(12,28123) if is_abundant(i)]
print("List of abundant numbers: " + str(abundant_numbers))

def can_be_sum_of_abundant(x):
    x_list =[]
    for i in (a for a in abundant_numbers if a <x):
        for j in (a for a in abundant_numbers if a <x):
            if i + j == x:
                print(" " + str(i) + " + " + str(j) + "=" + str(x) )
                return True
    return False

result = sum(int(i) for i in range (1,28123) if not can_be_sum_of_abundant(i))
print("result: " + str(result))









#result = sum(int(i) for i in range(1,28123) if not abundant_sum(i))


