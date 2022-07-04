def fibonacci(vector, n):
    if n == 1:
        return vector[-1]

    return fibonacci([*vector, vector[-1] + vector[-2]], n - 1)


print(fibonacci([1, 1], int(input())))
