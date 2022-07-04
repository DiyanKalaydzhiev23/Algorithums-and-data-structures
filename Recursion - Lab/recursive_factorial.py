def sum_factorial(n):
    if n == 0:
        return 1

    return n * sum_factorial(n - 1)


print(sum_factorial(int(input())))
