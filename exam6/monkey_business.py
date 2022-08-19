def variations(idx):
    global solutions

    if idx >= n:
        if sum(expressions) == 0:
            solutions += 1
            print(expressions)
        return

    expressions[idx] = numbers[idx]
    variations(idx + 1)

    expressions[idx] = -numbers[idx]
    variations(idx + 1)


n = int(input())
numbers = [num for num in range(1, n + 1)]
expressions = [0] * n
solutions = 0

variations(0)
print(f"Total Solutions: {solutions}")
