def factorial(z):
    if z == 1:
        return 1
    else:
        return z * factorial(z - 1)


def binomial_coefficient(n, k):
    print(factorial(n))
    a = (factorial(n)) / (factorial(k) * factorial(n - k))
    return a


n = int(int(input()))
k = int(input())
print(int(binomial_coefficient(n, k)))
