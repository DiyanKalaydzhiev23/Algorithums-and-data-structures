first = input()
second = input()

rows = len(first) + 1
cols = len(second) + 1
lcs = [[0] * cols for _ in range(rows)]

for row in range(1, rows):
    for col in range(1, cols):
        if first[row - 1] == second[col - 1]:
            prev = lcs[row - 1][col - 1]
            lcs[row][col] = prev + 1
        else:
            up = lcs[row - 1][col]
            left = lcs[row][col - 1]
            lcs[row][col] = max(up, left)

print(lcs[rows - 1][cols - 1])
