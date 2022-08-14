def count_ways(n):
    prev = 1
    prev2 = 1

    for i in range(2, n + 1):
        curr = prev + prev2
        prev2 = prev
        prev = curr

    return prev


print(count_ways(int(input())))
