#1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
import time
def trianagle_numbers():
     n = 1
     t = n
     while True:     # 1st iteration t =1, yield t, n =2 ,t =3 ,yield 3
         yield t     # 2 itera n =3 ,t =6, yield 6
         n +=1
         t += n


def count_factors(n): # return of the list of factors +2 ( self and 1)
    count = 2
    for i in range(1, n):
        if n % i == 0:
            count +=1
    return count



if __name__ == "__main__":
    start = time.time()
    triangles = trianagle_numbers()
    while True:
         triangle = next(triangles)
         c = count_factors(triangle)
         if c > 200:
             solution = triangle
             break
    elapsed = time.time() - start
    print("Solution {} is found for {} seconds".format(str(solution), elapsed))


