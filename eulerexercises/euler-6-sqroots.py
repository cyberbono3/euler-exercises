def sum_sq(n):
    return sum(x * x for x in range(1, n + 1))


def sq_sum(n):
    return (sum(x for x in range(1, n + 1))) ** 2


if __name__ == "__main__":
    solution = sq_sum(100) - sum_sq(100)
    print("Solution is found: " + str(solution))
